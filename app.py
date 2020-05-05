from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():
    response_data={}
    response_data['message'] = "Welcome"
    response_data['status'] = "Success"
    response=jsonify(response_data)
    return response