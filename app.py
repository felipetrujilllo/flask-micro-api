from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 19.99},
]
@app.get("/")
def home():
    return jsonify(
        message="Flask Micro-API is running",
        endpoints=["/hello", "/data"],
    )

@app.get("/hello")
def hello():
    return jsonify(message="Welcome to my Flask Micro-API!")

@app.get("/data")
def get_data():
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True, port=5001)