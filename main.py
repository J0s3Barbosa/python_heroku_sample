# coding=utf-8
from datetime import datetime
from flask import Flask, jsonify, request, abort
from flask.templating import render_template
from app.todo_module import todoModule
from app.utils_module import utils_module
from app.article_module import articleModule
from datetime import datetime


app = Flask(__name__)
app.register_blueprint(todoModule)
app.register_blueprint(articleModule)
app.register_blueprint(utils_module)


@app.route('/')
def starterPage():
    return render_template('Main_Template.html')

@app.route('/healthCheck')
def healthCheck():
    return 'Main app is Working!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/blog')
def blog():
        return render_template('bloglayout.html')


    
if __name__ == '__main__':
    app.run()
