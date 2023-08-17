#!/usr/bin/env python3
"""flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

auth_inst = Auth()
app = Flask(__name__)


@app.get('/', strict_slashes=False)
def index():
    """Index route on GET"""
    return jsonify({"message": "Bienvenue"}), 200


@app.post('/users', strict_slashes=False)
def users():
    """Register a user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        auth_inst.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except ValueError:
        jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
