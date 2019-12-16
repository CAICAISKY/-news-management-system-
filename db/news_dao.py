from db.mysql_db import pool


class NewsDao:
    """新闻数据操作类"""

    def search_unreview_list(self, page):
        """
        查询为审核新闻列表
        :param page: 查询页数
        :return: 新闻列表
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "WHERE n.state=%s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ("待审批", (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_list(self, page):
        """查询新闻列表"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_unreview_count_page(self):
        """计算待审批新闻的总页数"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s"
            cursor.execute(sql, ["待审批"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_count_page(self):
        """查询新闻的总页数"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update_unreview_news(self, news_id):
        """
        审批新闻
        :param news_id: 新闻id
        """
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state=%s WHERE id=%s"
            cursor.execute(sql, ["已审批", news_id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_by_id(self, news_id):
        """
        根据新闻ID删除新闻
        :param news_id: 新闻的id
        """
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id=%s"
            cursor.execute(sql, [news_id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def insert(self, title, editor_id, type_id, content_id, is_top):
        """
        新增新闻
        :param title: 新闻标题
        :param editor_id: 作者id
        :param type_id: 新闻类型
        :param content_id: 内容id
        :param is_top: 是否指定(0-5) 0表示不置顶
        :return:
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "INSERT INTO t_news(title, editor_id, type_id, content_id, is_top, state) " \
                  "VALUES(%s, %s, %s, %s, %s, %s)"
            con.start_transaction()
            cursor.execute(sql, (title, editor_id, type_id, content_id, is_top, "待审批"))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_cache(self, news_id):
        """查询新闻信息用于缓存到redis中"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, u.username, t.type, n.content_id, n.is_top, n.create_time " \
                  "FROM t_news n " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "JOIN t_type t ON n.type_id=t.id " \
                  "WHERE n.id=%s"
            cursor.execute(sql, [news_id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_by_id(self, id):
        """根据id查询新闻信息"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title, t.type, n.is_top " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id=t.id " \
                  "WHERE n.id=%s"
            cursor.execute(sql, [id])
            return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update_by_id(self, id, title, type_id, content_id, is_top):
        """更新新闻信息"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "UPDATE t_news " \
                  "SET title=%s, type_id=%s, is_top=%s, content_id=%s, state=%s " \
                  "WHERE id=%s"
            cursor.execute(sql, (title, type_id, is_top, content_id, "待审批", id))
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
