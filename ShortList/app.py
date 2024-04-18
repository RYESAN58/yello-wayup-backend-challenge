from flask import Flask, jsonify


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)