# coding:utf-8
# time: 2023/5/9

"""
学生信息库
"""

students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
}


def get_all_students():
    for stu_id, value in students.items():
        print(
            f'学号：{stu_id},姓名：{value["name"]}, 年龄：{value["age"]}, '
            f'班级： {value["class_number"]}, 性别：{value["sex"]}')


def add_student(**kwargs):
    if 'name' not in kwargs:
        print('没有学生姓名！')
        return
    if 'age' not in kwargs:
        print('缺少学生年龄')
        return
    if 'class_number' not in kwargs:
        print('缺少班级号')
        return
    if 'sex' not in kwargs:
        print('缺少性别信息！')
        return
    stu_id = max(students) + 1
    students[stu_id] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'class_number': kwargs['class_number'],
        'sex': kwargs['sex']
    }


def delete_student(stu_id):
    if stu_id not in students:
        print('该学生不存在')
        return None

    pop = students.pop(stu_id)
    print('{} 同学的信息已经被删除！'.format(pop.get('name')))


def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return '没有发现学生姓名'
    if 'age' not in kwargs:
        return '缺少学生年龄'
    if 'sex' not in kwargs:
        return '缺少学生性别'
    if 'class_number' not in kwargs:
        return '缺少学生班级'
    return True


def update_student(student_id, **kwargs):
    if student_id not in students:
        print('并不存在这个学号:{}'.format(student_id))

    check = check_user_info(**kwargs)
    if not check:
        print(check)
        return

    students[student_id] = kwargs
    print('同学信息更新完毕')


def get_user_by_id(student_id):
    return students.get(student_id)


def search_users(**kwargs):
    values = list(students.values())
    key = None
    value = None
    result = []

    if 'name' in kwargs:
        key = 'name'
        value = kwargs[key]
    elif 'sex' in kwargs:
        key = 'sex'
        value = kwargs['sex']
    elif 'class_number' in kwargs:
        key = 'class_number'
        value = kwargs[key]
    elif 'age' in kwargs:
        key = 'age'
        value = kwargs[key]
    else:
        print('没有发现搜索的关键字')
        return

    for user in values:
        if user[key] == value:
            result.append(user)
    return result


if __name__ == '__main__':
    users = search_users(age=33)
    print(users)
