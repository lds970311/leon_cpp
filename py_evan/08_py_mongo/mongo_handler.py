# coding:utf-8
# time: 2023/5/21
# author: evan

from mongo_collection import client


def insert_data():
    client.school.student.insert_many([
        {'name': 'Ada', 'age': 32, 'sex': 'female', 'address': 'NYC', 'hobbies': ['basketball', 'football']},
        {'name': 'Louis', 'age': 35, 'sex': 'male', 'address': 'NYC', 'hobbies': ['basketball', 'football']},
        {'name': 'Sam', 'age': 31, 'sex': 'male', 'address': 'CA', 'hobbies': ['basketball', 'football', 'volleyball']}
    ])


def search_data():
    result = client.school.student.find({'address': 'NYC'})
    for item in result:
        print(item)
    # for k, v in result.items():
    #     print(k, ':', v)


def update():
    client.school.student.update_many(
        {'address': 'NYC'},
        {'$set': {'address': 'Los Santoes'}}
    )


def delete():
    client.school.student.delete_many(
        {'address': {'$ne': 'Los Santoes'}}
    )


if __name__ == '__main__':
    # insert_data()
    # search_data()
    # update()
    delete()
