from urllib import request
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import re
import hashlib
import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # '///' is a relative path from the current directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # This flag disables the signal for object modifications

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(164), index=True)
    encoded = db.Column(db.String(64), index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'encoded': self.encoded,
        }
    def __repr__(self):
        return '<Url {}>'.format(self.url)


with app.app_context():
    db.create_all()

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
        return short_id + ".co"
    return url

@app.route('/encode' , methods = ['POST'])
def encode():
    data = request.get_json()
    data['encoded'] = encodeUrl(data['url'])
    url = Url(url = data['url'], encoded = data['encoded'])
    try:
        db.session.add(url)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Error adding data to the database:", str(e))
    return jsonify(data)

@app.route('/urls')
def get_urls():
    all_urls = Url.query.all()
    return jsonify([url.to_dict() for url in all_urls])


if __name__ == '__main__':
    app.run(debug=True)