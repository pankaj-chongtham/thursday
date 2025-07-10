from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Hello, Thursday!"})
