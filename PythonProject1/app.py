from flask import Flask
import db
import send
app = Flask(__name__)


@app.route('/get')
def hello_world():
  return 'Hello, World!'

@app.route('/user/<username>', methods=['POST'])
def show_user_profile(username):
    return f'Hello, {username}'

@app.route('/users')
def show_users():
    return send.getMessage(db.getUsers())

if __name__ == '__main__':
    app.run()