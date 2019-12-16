from db.news_dao import NewsDao


class NewsService:
    """新闻业务层"""

    __news_dao = NewsDao()

    def search_unreview_list(self, page):
        """查询待审批新闻列表"""
        result = self.__news_dao.search_unreview_list(page)
        return result

    def search_list(self, page):
        """查询新闻列表"""
        result = self.__news_dao.search_list(page)
        return result

    def search_unreview_count_page(self):
        """查询待审批新闻的总页数"""
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    def search_count_page(self):
        """查询新闻的总页数"""
        count_page = self.__news_dao.search_count_page()
        return count_page

    def update_unreview_news(self, news_id):
        """审批新闻"""
        self.__news_dao.update_unreview_news(news_id)

    def delete_by_id(self, news_id):
        """根据新闻id删除新闻"""
        self.__news_dao.delete_by_id(news_id)

    def insert(self, title, editor_id, type_id, content_id, is_top):
        """新增新闻"""
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)
