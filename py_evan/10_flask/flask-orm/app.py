# coding:utf-8
# time: 2023/5/28
# author: evan
import os
import random

from flask import Flask, render_template
from werkzeug.utils import secure_filename

from forms import LoginForm
from model import LoginUser, db, User

app = Flask(__name__, template_folder='./templates')

# 配置sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:19970311@localhost:3306/flask'

# 配置WTF表单
app.config['WTF_CSRF_SECRET_KEY'] = 'evan666666'
app.secret_key = 'secret_key_evan'
app.config['WTF_CSRF_ENABLED'] = False

# 创建模型
db.init_app(app)


@app.route('/add_user')
def add_user():
    for i in range(1, 101):
        user = User(id=i + 5, username=f'beijing_{i}', age=21 + i)
        db.session.add(user)
        db.session.commit()

    return 'user add success'


@app.route('/del_user')
def del_user():
    user = User.query.filter_by(age=21).first()
    db.session.delete(user)
    db.session.commit()

    return 'del success'


@app.route('/query/<int:page>/')
def search_user(page):
    all_user = User.query
    paginate = all_user.paginate(page=page, per_page=10)

    return render_template('list_user.html', users=paginate)


@app.route('/form', methods=['POST', 'GET'])
def page_form():
    """
    wtf表单
    :return:
    """
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username, password)
        login_user = LoginUser(id=random.randint(10, 90000), username=username, password=password)
        db.session.add(login_user)
        db.session.commit()

        # 获取图片
        img = form.avatar.data
        f_name = secure_filename(img.filename)
        path = os.path.join(os.path.dirname(__name__), 'imgs', f_name)
        img.save(path)
    else:
        print(form.errors)

    return render_template("page_form.html", form=form)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
