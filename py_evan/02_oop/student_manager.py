# coding:utf-8
# time: 2023/5/10

import json
import logging
import os


class LackArgsError(Exception):
    def __init__(self, msg):
        self.msg = msg


class JsonPathNotFoundError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NotFileError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NotJsonError(Exception):
    def __init__(self, msg):
        self.msg = msg


class StudentManager:
    """
    学生管理系统
    """

    def __init__(self, json_path, log_path) -> None:

        self.json_path = json_path
        self.log_path = log_path
        self.__init_log()
        self.__check_path()
        self.__load_data()

    def __init_log(self):
        mode = ''
        if not os.path.exists(self.log_path):
            mode = 'w'
        else:
            mode = 'a'

        logging.basicConfig(
            filename=self.log_path,
            level=logging.DEBUG,
            format='%(asctime)s %(filename)s [line=%(lineno)s %(levelname)s %(message)s]',
            filemode=mode
        )

        self.log = logging

    def __load_data(self):
        with open(self.json_path, 'r') as f:
            try:
                data = f.read()
            except Exception as e:
                raise e
        self.students = json.loads(data)

    def __write_data(self):
        with open(self.json_path, 'w') as f:
            try:
                str = json.dumps(self.students)
            except Exception as e:
                raise e

            f.write(str)

    def __check_path(self):
        """
        检查path是否合法
        :return:
        """
        if not os.path.exists(self.json_path):
            raise JsonPathNotFoundError("该文件不存在！")

        if not os.path.isfile(self.json_path):
            raise NotFileError("不是一个文件")

        if not self.json_path.endswith(".json"):
            raise NotJsonError("不是一个json文件")

    def get_all(self):
        for stu_id, value in self.students.items():
            print(
                f'学号：{stu_id},姓名：{value["name"]}, 年龄：{value["age"]}, '
                f'班级： {value["class_number"]}, 性别：{value["sex"]}')

    def check_info(self, **kwargs) -> None:
        assert len(kwargs) == 4, '参数必须是4个！'

        if 'name' not in kwargs:
            raise LackArgsError('没有发现学生姓名')
        if 'age' not in kwargs:
            raise LackArgsError('缺少学生年龄')
        if 'sex' not in kwargs:
            raise LackArgsError('缺少学生性别')
        if 'class_number' not in kwargs:
            raise LackArgsError('缺少学生班级')

        name_val = kwargs['name']
        age_val = kwargs['age']
        sex_val = kwargs['sex']
        class_number_val = kwargs['class_number']

        if not isinstance(name_val, str):
            raise TypeError('name 应该为 str类型')

        if not isinstance(age_val, int):
            raise TypeError('age 应该为 int类型')

        if not isinstance(sex_val, str):
            raise TypeError('sex 应该为 str类型')

        if not isinstance(class_number_val, str):
            raise TypeError('class_number 应该为 str类型')

    def add(self, **kwargs):
        try:
            self.check_info(**kwargs)
        except (LackArgsError, TypeError) as e:
            print(e)
        k = list(self.students.keys())
        lds = []
        for i in k:
            lds.append(int(i))
        stu_id = max(lds)
        self.students[stu_id] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'class_number': kwargs['class_number'],
            'sex': kwargs['sex']
        }
        self.__write_data()
        self.__load_data()

    def delete(self, stu_id):
        if stu_id not in self.students:
            print('该学生不存在')
            return None

        pop = self.students.pop(stu_id)
        self.__write_data()
        self.__load_data()
        self.log.info('{} 同学的信息已经被删除！'.format(pop.get('name')))

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        try:
            self.check_info(**kwargs)
        except (LackArgsError, TypeError) as e:
            print(e)
        self.students[student_id] = kwargs
        self.__write_data()
        self.__load_data()
        # print('同学信息更新完毕')
        self.log.info(f'学号为{student_id} 的信息更新成功！')

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def search(self, **kwargs):
        assert len(kwargs) == 1, '参数应该为1个'

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
            try:
                self.check_info(**student)
            except (LackArgsError, TypeError) as e:
                print(e)
                continue
            self.__add(**student)
        self.__write_data()
        self.__load_data()

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
            try:
                id_ = list(student.keys())[0]
            except IndexError as e:
                print(e)
                continue
            if id_ not in self.students:
                print(f'学号{id_} 不存在')
                continue
            user_info = student[id_]
            try:
                self.check_info(**user_info)
            except (LackArgsError, TypeError) as e:
                print(e)
                continue
            self.students[id_] = user_info
        self.__write_data()
        self.__load_data()
        print('所有用户信息更新完成')


if __name__ == '__main__':
    sm = StudentManager('student.json', 'student.log')
    sm.get_all()
    sm.add(name='leon', age=33, class_number='C', sex='boy')
    # sm.delete('5')
    sm.update('4', name='evan', age=33, class_number='C', sex='girl')
    print(sm.get_by_id('2'))
