from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def vanhu():
    users = {
        'name': 'donty',
        'name1': 'hussein',
        'name3': 'hameno'
    }
    return users

if __name__ == '__main__':
    app.run()