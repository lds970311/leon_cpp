# coding:utf-8
# time: 2023/5/21
# author: evan
# gridfs操作
import datetime

from bson import ObjectId
from gridfs import GridFS

from mongo_collection import client

db = client.school
gfs = GridFS(db, collection='book')


def upload_file():
    file = open('./scripts/mongo.sql', 'rb')
    args = {'type': 'sql'}
    gfs.put(file, **args)
    file.close()


def find_file():
    files = gfs.find_one({'type': 'sql'})
    print(files.type)
    print(files.length / 1024 ** 2)
    print(files.uploadDate + datetime.timedelta(hours=8))


def is_exists():
    exists = gfs.exists(**{'type': 'sql'})
    print(exists)


def download_file():
    files = gfs.find_one({'type': 'sql'})
    d_file = gfs.get(ObjectId(files._id))
    f = open('./download.sql', 'wb')
    f.write(d_file.read())
    f.close()


def delete_file():
    files = gfs.find_one({'type': 'sql'})
    gfs.delete(ObjectId(files._id))


if __name__ == '__main__':
    # find_file()
    # is_exists()
    # download_file()
    delete_file()
