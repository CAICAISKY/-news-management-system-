from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    def login(self, username, password):
        """用户登陆"""
        result = self.__user_dao.login(username, password)
        return result

    def search_user_role(self, username):
        """查询用户角色"""
        role = self.__user_dao.search_user_role(username)
        return role
