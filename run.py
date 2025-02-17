from src import UserRepo
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Ola, estou na aplicação setada"


@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.get_json()
    userRepo.insert_user(body["name"])
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
