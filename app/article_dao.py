# coding=utf-8
import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime


class ArticleDAO:

    def __init__(self, database):
        self.database = database
        self.article_collection = self.database.article

    def create(self, data):
        article = {
            'title': data.get('title'),
            'description': data.get('description'),
            'addedAt': datetime.utcnow(),
        }

        inserted_id = self.article_collection.insert_one(article).inserted_id
        article = self.article_collection.find_one({ '_id': ObjectId(inserted_id) })

        return self.to_json(article)

    def list(self):
        articles = self.article_collection.find().sort('done', pymongo.ASCENDING)
        return self.to_json(articles)

    def read(self, object_id):
        article = self.article_collection.find_one({ '_id': ObjectId(object_id)})
        return self.to_json(article)

    def update(self, object_id, data):
        records_updated = self.article_collection.update_one({"id": int(object_id)}, data)
        return self.to_json(records_updated)


    def delete(self, object_id):
        article = self.article_collection.find_one({ '_id': ObjectId(object_id)})
        result = self.article_collection.delete_one(article)
        print(result.deleted_count, " documents deleted.")
        return result

    def to_json(self, data):
        return json.loads(json_util.dumps(data))
