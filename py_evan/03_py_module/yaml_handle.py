# coding:utf-8
# time: 2023/5/11
# author: evan
# python操作yaml文件

import yaml


def yaml_handle():
    with open('./TestFiles/message.yaml', 'r') as file, open('./TestFiles/message.yaml', 'a') as file2:
        data = yaml.load(file, Loader=yaml.FullLoader)
        # print(data)
        print(type(data))
        types = data['types']
        py = data['python']
        print(types)
        print(py)
        # 写入内容
        content = {
            'java': ['spring', 'springmvc', 'mybatis-plus', 'rabbitmq']
        }
        yaml.dump(content, file2)


if __name__ == '__main__':
    yaml_handle()
