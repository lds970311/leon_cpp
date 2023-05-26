# coding:utf-8
# time: 2023/5/25
# author: evan
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello 145!'


@app.route('/hello')
def hello():
    user = {
        'name': 'evan',
        'age': 21
    }

    return render_template('hello.html', user=user)


@app.route('/man')
def man():
    man = {
        'name': 'zs',
        'age': 30,
        'hobby': (1, 2, 3, 4, 5),
        'address': 'Beijing'
    }

    return json.dumps(man)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
