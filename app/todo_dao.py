# coding=utf-8
import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId

class TodoDAO:

    def __init__(self, database):
        self.database = database
        self.task_collection = self.database.task

    def create(self, data):
        task = {
            'title': data.get('title'),
            'description': data.get('description'),
            'done': bool(data.get('done')) 

        }

        inserted_id = self.task_collection.insert_one(task).inserted_id
        task = self.task_collection.find_one({ '_id': ObjectId(inserted_id) })

        return self.to_json(task)

    def list(self):
        tasks = self.task_collection.find().sort('done', pymongo.ASCENDING)
        return self.to_json(tasks)

    def read(self, object_id):
        # task = self.task_collection.find_one({ '_id': ObjectId(object_id)})
        task = self.task_collection.find_one({ '_id': ObjectId(object_id)}, {'_id': False})
        return self.to_json(task)

    def update(self, object_id, data):
        try:
            records_updated = self.task_collection.update_one({"_id": ObjectId(object_id)},  {'$set': data} )
            return records_updated.matched_count
        except Exception as error:
            raise Exception(error)
 

    def delete(self, object_id):
        task = self.task_collection.find_one({ '_id': ObjectId(object_id)})
        result = self.task_collection.delete_one(task)
        print(result.deleted_count, " documents deleted.")
        return result

    def to_json(self, data):
        return json.loads(json_util.dumps(data))
