# coding=utf-8
import json
from flask import jsonify, request, Blueprint
from app.article_dao import ArticleDAO
import pymongo
from flask.templating import render_template
from app.config.app_config import mongo_config


articleModule = Blueprint('article', __name__,
                        template_folder='templates')

try:
    client = pymongo.MongoClient(mongo_config['mongo_connection'])
    database = client.article
    article_dao = ArticleDAO(database)
except Exception as exc:
    print(exc)
# log


class ArticleModule():

    @articleModule.route('/articles')
    def articles():
        list = article_dao.list()
        print(list)
        return render_template('articles.html', data=list)

    @articleModule.route('/articlehc')
    def articlehc():
        return 'articles module is Working!'

    @articleModule.route('/articlelist')
    def articlelist():
        return jsonify(article_dao.list()), 200

    @articleModule.route('/articles/<pk>', methods=['GET', 'PUT'])
    def get(pk):
        
        if request.method == 'GET':
            return jsonify(article_dao.read(pk))
        
        if request.method == 'PUT':
            """
            Function to update .
            """
            try:
                # Get the value which needs to be updated
                try:
                    body = jsonify(article_dao.read(pk))
                except:
                    # Bad request as the request body is not available
                    # Add message for debugging purpose
                    return "", 400

                # Updating the user
                records_updated =  article_dao.update(pk, request.form) 

                # Check if resource is updated
                if records_updated.modified_count > 0:
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

    @articleModule.route('/articles', methods=['POST'])
    def create():
        if request.method == 'POST':
            print(request.form)
            data = request.form
            title = data.get('title', None)
            description = data.get('description', None)

            if not title or not description:
                return "The fields 'title' and 'description' are required", 400

            task = article_dao.create(data)

            return jsonify(task), 201

    @articleModule.route('/articles/<pk>', methods=['DELETE'])
    def delete(pk):
        print('delete(pk):')
        print(pk)
        if request.method == 'DELETE':
            try:
                # Delete the user
                delete_user =  article_dao.delete(pk) 

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

     
    
