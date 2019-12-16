from db.mysql_db import pool


class TypeDao:
    """新闻类型数据库操作类"""

    def search_list(self):
        """查询新闻类型列表"""
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id,type FROM t_type ORDER BY id"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
