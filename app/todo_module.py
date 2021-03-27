# coding=utf-8
from app.todo_dao import TodoDAO
import json
from bson import json_util
from flask import Flask, jsonify, request, abort, Blueprint
import pymongo
from flask.templating import render_template
import json
from app.config.app_config import mongo_config

todoModule = Blueprint('todos', __name__,
                        template_folder='templates')

try:
    client = pymongo.MongoClient(   
                                 mongo_config['mongo_connection'])
    database = client.todo_list
    tasks_dao = TodoDAO(database)
except Exception as exc:
    print(exc)
# log


class TodoModule():

    @todoModule.route('/tasks')
    def tasks():
        list = tasks_dao.list()
        return render_template('tasks.html', data=list)

    @todoModule.route('/todohc')
    def todohc():
        return 'todo module is Working!'

    @todoModule.route('/tasklist')
    def tasklist():
        return jsonify(tasks_dao.list()), 200

    @todoModule.route('/tasks/<pk>', methods=['GET', 'PUT'])
    def get(pk):
        print(pk)
        if request.method == 'GET':
            print('GET')
            return jsonify(tasks_dao.read(pk))
        if request.method == 'PUT':
            print('PUT')
            
            """
            Function to update .
            """
            try:
                # Get the value which needs to be updated
                try:
                    data_from_db = tasks_dao.read(pk)
                except:
                    # Bad request as the request body is not available
                    # Add message for debugging purpose
                    return "", 400

                # Updating the user
                obj_to_update = json.loads(request.form.get("data"))
                print(obj_to_update)
                print(data_from_db)
                if obj_to_update != data_from_db:
                    print(obj_to_update != data_from_db)
                    records_updated =  tasks_dao.update(pk, obj_to_update) 
                    # Check if resource is updated
                    if records_updated > 0:
                        # Prepare the response as resource is updated successfully
                        return "", 200
                else:
                    # Bad request as the resource is not available to update
                    # Add message for debugging purpose
                    return "", 404
            except:
                # Error while trying to update the resource
                # Add message for debugging purpose
                return "", 500

    @todoModule.route('/tasks', methods=['POST'])
    def create():
        if request.method == 'POST':
            data = request.form
            title = data.get('title', None)
            description = data.get('description', None)

            if not title or not description:
                return "The fields 'title' and 'description' are required", 400

            task = tasks_dao.create(data)

            return jsonify(task), 201

    @todoModule.route('/tasks/<pk>', methods=['DELETE'])
    def delete(pk):
        if request.method == 'DELETE':
            try:
                # Delete the user
                delete_user =  tasks_dao.delete(pk) 

                if delete_user.deleted_count > 0 :
                    # Prepare the response
                    return "", 200
                else:
                    # Resource Not found
                    return "", 404
            except:
                # Error while trying to delete the resource
                # Add message for debugging purpose
                return "", 500      

     
    
