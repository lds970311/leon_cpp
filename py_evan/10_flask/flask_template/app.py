# coding:utf-8
# time: 2023/5/27
# author: evan

from flask import Flask, render_template, flash

app = Flask(__name__, template_folder='./templates')
app.secret_key = 'secret_key_evan'


@app.route('/')
def index():
    """  首页 """
    return render_template('index.html')


@app.route('/course')
def course():
    """  免费课程 """
    return render_template('course.html')


@app.route('/coding')
def coding():
    """  实战课程 """
    return render_template('coding.html')


@app.route('/article')
def article():
    """  手记 """
    return render_template('article.html')


@app.route('/wenda')
def wenda():
    """  实战课程 """
    return render_template('wenda.html')


@app.route('/flash')
def flash_msg():
    """
    消息闪现
    :return:
    """
    flash('hahaha', 'warn')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=16666, debug=True)
