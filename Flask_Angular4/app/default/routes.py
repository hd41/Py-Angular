from . import default
from flask import request,jsonify,make_response
from flask import Flask
from flask_cors import CORS,cross_origin

CORS(default)

@default.route('/')
def home():
    return default.send_static_file('index.html')

@default.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        json_data = request.get_json()
        email=json_data.get('email')
        password=json_data.get('password')
        responseObject = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
        return jsonify(responseObject)

@default.route('/register', methods = ['GET','POST'])
def register():
    json_data = request.get_json
    email=json_data.get('email')
    password=json_data.get('password')
    print email+" "+password
