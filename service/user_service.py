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

    def insert_user(self, username, password, email, role_id):
        """添加用户"""
        self.__user_dao.insert_user(username, password, email, role_id)

    def update_by_id(self, user_id, username, password, email, role_id):
        """修改用户"""
        self.__user_dao.update_by_id(user_id, username, password, email, role_id)

    def delete_by_id(self, user_id):
        """删除用户"""
        self.__user_dao.delete_by_id(user_id)

    def search_count_page(self):
        """查询用户总页数"""
        count_page = self.__user_dao.search_count_page()
        return count_page

    def search_list(self, page):
        """查询用户列表"""
        result = self.__user_dao.search_list(page)
        return result

    def search_by_username(self, username):
        """根据用户名查找用户"""
        return self.__user_dao.search_by_username(username)
