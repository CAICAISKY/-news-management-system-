from db.type_dao import TypeDao


class TypeService:
    """新闻类型业务层"""

    __type_dao = TypeDao()

    def search_list(self):
        """查询新闻类型列表"""
        return self.__type_dao.search_list()
