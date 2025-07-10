from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Hello, Thursday!"})

@app.route('/thursday', methods=['GET'])
def thursday():
    return jsonify({"message": "Wow! API and CICD works!!!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
