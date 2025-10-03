from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow React to fetch from a different port

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello from Flask!"
    # OR return jsonify({"message": "Hello"}) if you want JSON

if __name__ == "__main__":
    app.run(debug=True)