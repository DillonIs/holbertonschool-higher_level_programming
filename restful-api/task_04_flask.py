#!/usr/bin/python3
"""task_04_flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def json_data():
    return jsonify(list(users))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def username(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data_user = request.get_json()
    new_username = data_user.get("username")
    if not new_username:
        return jsonify({"error": "Username is required"}), 400
    users[new_username] = data_user
    return jsonify({"message": "User added", "user": data_user}), 201

if __name__ == "__main__":
    app.run()
