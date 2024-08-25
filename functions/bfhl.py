from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        user_id = "john_doe_17091999"  # replace with your user ID generation logic
        email = "john@xyz.com"
        roll_number = "ABCD123"
        
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase = [max([char for char in data if char.islower()], default="")]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase,
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

import serverless_wsgi

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
