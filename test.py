from db.news_dao import NewsDao
from db.role_dao import RoleDao

from service.news_service import NewsService
from service.user_service import UserService

news_service = NewsService()
news_dao = NewsDao()

user_service = UserService()

role_dao = RoleDao()


# result = news_dao.search_unreview_list(1)
# pages = news_dao.search_unreview_count_page()
# print(pages)

user_service.insert_user("Schuyler", 123456, "caishunwei@126.com", 1)
