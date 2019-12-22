from bson import ObjectId

from db.mongo_db import db


class MongoDao:
    """MongoDB数据库操作类"""
    def insert(self, content):
        """
        保存新闻文件
        :param content: 文档内容
        :return: 保存结果
        """
        return db.insert_one({"content": content})

    def update(self, content_id, content):
        """
        修改新闻正文
        :param content_id: 正文id
        :param content: 新内容
        """
        db.update_one({"_id": ObjectId(content_id)}, {"$set": {"content": content}})

    def search_content_by_id(self, content_id):
        """
        根据新闻id查找新闻正文
        :param content_id: 正文id
        :return: 正文内容
        """
        result = db.find_one({"_id": ObjectId(content_id)})
        return result["content"]

    def delete_by_id(self, content_id):
        """
        根据id删除新闻内容
        :param content_id:
        """
        db.delete_one({"_id": ObjectId(content_id)})
