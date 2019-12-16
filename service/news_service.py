from db.news_dao import NewsDao
from db.redis_dao import RedisDao


class NewsService:
    """新闻业务层"""

    __news_dao = NewsDao()
    __redis_dao = RedisDao()

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

    def search_cache(self, news_id):
        """查询新闻信息用于缓存到redis中"""
        result = self.__news_dao.search_cache(news_id)
        return list(result)

    def cache_news(self, news):
        """缓存新闻信息到redis中"""
        news_id = str(news[0])
        title = news[1]
        editor = news[2]
        type = news[3]
        is_top = news[5]
        create_time = str(news[6])
        content = news[7]
        self.__redis_dao.insert(news_id, title, editor, type, content, is_top, create_time)
