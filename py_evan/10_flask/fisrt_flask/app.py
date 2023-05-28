# coding:utf-8
# time: 2023/5/25
# author: evan
import json

from flask import Flask, render_template, request, \
    make_response, redirect

app = Flask(__name__, template_folder='./templates')


# 添加break， continue扩展


@app.route('/')
def hello_world():  # put application's code here
    redirect('/hello')
    return 'Hello 145!'


@app.route('/hello')
def hello():
    user = {
        'name': 'evan',
        'age': 21
    }

    return render_template('hello.html', user=user)


@app.route('/page/<int:id>')
def page(id):
    # print(json.dumps(current_app))
    # print(json.dumps(g))
    print(request.method)
    print(request.headers)
    print(request.args)
    return f'id:{id}'


@app.before_first_request
def before_fr():
    print('before_first_request')


@app.before_request
def before_request():
    print('before request')


@app.route('/man')
def man():
    man = {
        'name': 'zs',
        'age': 30,
        'hobby': (1, 2, 3, 4, 5),
        'address': 'Beijing'
    }

    return json.dumps(man)


@app.route('/resp')
def response():
    return make_response()


@app.route('/html')
def render_html():
    with open('./templates/test.html', 'r') as f:
        content = f.read()

    return make_response(content, 200)


@app.route('/condition')
def condition():
    age = 32

    return render_template('condition.html', age=age)


@app.route('/condition_for')
def condition_for():
    list_user = [
        {'username': '张三', 'age': 32, 'address': '北京'},
        {'username': '李四', 'age': 22}
    ]

    return render_template('condition.html', list_user=list_user)


@app.route('/filter')
def filter_test():
    phone_num = '15544445642'
    return render_template('filter.html', phone_num=phone_num)


@app.template_filter('num_filter')
def num_filter(num):
    '*'
    return num[0:3] + "****" + num[7:]


@app.route('/macro')
def macro():
    """
    模板中使用宏
    :return:
    """
    return render_template("/macro.html")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    print(app.url_map)
