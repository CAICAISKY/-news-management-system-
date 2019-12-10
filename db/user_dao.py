from db.mysql_db import pool


class UserDao:
    """用户数据表操作类"""


    def login(self, username, password):
        """
        用户登陆
        :param username: 用户名字
        :param password: 用户密码
        :return: 登陆结果
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user " \
                  "WHERE username=%s AND AES_DECRYPT(UNHEX(password),'HelloMysql')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_user_role(self, username):
        """
        查询用户角色
        :param username: 用户名
        :return: 角色类型
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role " \
                  "FROM t_user u JOIN t_role r ON u.role_id=r.id " \
                  "WHERE username=%s"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
