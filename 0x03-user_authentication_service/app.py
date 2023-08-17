from flask import Flask, jsonify, request, abort, redirect

app = Flask()


app.get('/', strict_slashes=False)
def index():
    """Index route on GET"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
