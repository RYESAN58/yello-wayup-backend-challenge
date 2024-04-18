from urllib import request
from flask import Flask, jsonify, request
import re
import hashlib
import base64

app = Flask(__name__)



url_mapping = {}


@app.route('/')

def index():
    return 'Hello, World!'

@app.route('/sample_json')
def sample_json():
    data = {
        "users": [
            {"id": 1, "name": "John Doe", "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
            {"id": 3, "name": "Emily Jones", "email": "emily@example.com"}
        ],
        "success": True,
        "message": "User data fetched successfully"
    }
    return jsonify(data)

def encodeUrl(url):
    pattern = re.compile(r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$')
    if (re.match(pattern, url)):
        url_hash = hashlib.sha256(url.encode('utf-8')).digest()
        short_id = base64.urlsafe_b64encode(url_hash).decode('utf-8')[:8]
        url_mapping[short_id] = url

        return short_id + ".co"
    return url

@app.route('/encode' , methods = ['POST'])
def encode():
    data = request.get_json()
    print(data)
    data['encoded'] = encodeUrl(data['url'])
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)