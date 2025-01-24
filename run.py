from src import UserRepo
from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    

@app.rout('/insert', methods=['GET'])
def insert():
    userRepo = UserRepo()
    body = request.json
    
    userRepo.insert_user(body["name"])
    
    return 'OK'
