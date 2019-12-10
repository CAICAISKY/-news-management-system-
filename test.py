from db.news_dao import NewsDao

from service.news_service import NewsService

news_service = NewsService()
news_dao = NewsDao()

result = news_dao.search_unreview_list(1)
# pages = news_dao.search_unreview_count_page()
# print(pages)
