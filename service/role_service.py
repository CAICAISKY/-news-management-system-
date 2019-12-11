from db.role_dao import RoleDao


class RoleService:
    """角色业务层"""

    __role_dao = RoleDao()

    def search_list(self):
        """查询角色列表"""
        result = self.__role_dao.search_list()
        return result
