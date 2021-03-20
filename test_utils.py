# coding=utf-8

from datetime import datetime
import json
import os
from bson import json_util
from app.config.app_config import mongo_config
import pytest

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def test_foo_bar():
       assert True

def test_values():
    data = {'{"title":"interview","description":"as 16","done":"on"}': ''}
    test = json.loads(json_util.dumps(data))
    assert test.title != ''

def test_get_conn_value():
    test_conn = mongo_config['mongo_connection']
    assert  test_conn != ''

def test_get_all_env():
    all_os = []
    for item in os.keys():
        all_os.add(item)
        print(item)
    assert  all_os.count > 0
    
    
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
