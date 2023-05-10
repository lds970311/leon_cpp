# coding:utf-8
# time: 2023/5/10


students_dict = {
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


class StudentManager:
    """
    学生管理系统
    """

    def __init__(self, students: dict) -> None:
        self.students = students

    def get_all(self):
        for stu_id, value in self.students.items():
            print(
                f'学号：{stu_id},姓名：{value["name"]}, 年龄：{value["age"]}, '
                f'班级： {value["class_number"]}, 性别：{value["sex"]}')

    def check_info(self, **kwargs) -> bool:
        if 'name' not in kwargs:
            print('没有发现学生姓名')
            return False
        if 'age' not in kwargs:
            print('缺少学生年龄')
            return False
        if 'sex' not in kwargs:
            print('缺少学生性别')
            return False
        if 'class_number' not in kwargs:
            print('缺少学生班级')
            return False
        return True

    def add(self, **kwargs):
        if self.check_info(**kwargs):
            stu_id = max(self.students) + 1
            self.students[stu_id] = {
                'name': kwargs['name'],
                'age': kwargs['age'],
                'class_number': kwargs['class_number'],
                'sex': kwargs['sex']
            }

    def delete(self, stu_id):
        if stu_id not in self.students:
            print('该学生不存在')
            return None

        pop = self.students.pop(stu_id)
        print('{} 同学的信息已经被删除！'.format(pop.get('name')))

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        check = self.check_info(**kwargs)
        if not check:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息更新完毕')

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def search(self, **kwargs):
        values = list(self.students.values())
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

    def adds(self, new_students):
        """
        批量添加
        :param new_students:
        :return:
        """
        for student in new_students:
            check = self.check_info(**student)
            if not check:
                print(check, student.get('name'))
                continue
            self.__add(**student)

    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def batch_delete(self, ids: list) -> None:
        """
        批量删除
        :param ids:
        :return:
        """
        for stu_id in ids:
            self.delete(stu_id)
        else:
            print("批量删除成功！")

    def batch_update(self, update_students):
        for student in update_students:
            id_ = list(student.keys())[0]
            if id_ not in self.students:
                print(f'学号{id_} 不存在')
                continue
            user_info = student[id_]
            check = self.check_info(**user_info)
            if not check:
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成')


if __name__ == '__main__':
    sm = StudentManager(students_dict)
    # sm.get_all()
    # sm.batch_delete([3, 4, 5])
    # sm.get_all()
    print(sm.search(age=18))
