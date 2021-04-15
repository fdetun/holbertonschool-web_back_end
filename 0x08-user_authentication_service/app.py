#!/usr/bin/env python3
""" flask app """
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def wlcm():
    """ welcome flask """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def registration():
    """ register new user app """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
