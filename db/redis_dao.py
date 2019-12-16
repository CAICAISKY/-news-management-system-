from db.redis_db import pool
import redis


class RedisDao:
    """redis操作类"""

    def insert(self, news_id, title, editor, news_type, content, is_top, create_time):
        """将已审批的新闻信息缓存到redis中"""
        con = redis.Redis(connection_pool=pool)
        try:
            con.hmset(news_id, {
                "title": title,
                "editor": editor,
                "type": news_type,
                "content": content,
                "is_top": is_top,
                "create_time": create_time
            })
            if is_top == 0:
                con.expire(news_id, 24*60*60)
        except Exception as e:
            print(e)
        finally:
            del con

    def delete(self, id):
        """删除数据"""
        con = redis.Redis(connection_pool=pool)
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con
