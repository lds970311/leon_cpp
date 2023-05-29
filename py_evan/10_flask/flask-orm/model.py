# coding:utf-8
# time: 2023/5/28
# author: evan

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class LoginUser(db.Model):
    __tablename__ = 'login_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)


class UserAddress(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
