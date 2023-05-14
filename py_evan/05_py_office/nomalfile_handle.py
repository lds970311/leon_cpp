# coding:utf-8
# time: 2023/5/13
# author: evan
# 普通文件操作
import glob
import hashlib
import os
import shutil


def copy_file():
    shutil.copy("./test_files/leon.txt", './test_files/leon_copied.txt')


def move_file():
    shutil.move('./test_files/leon.txt', 'doc')


def rm_file():
    os.remove('./doc/leon.txt')


def zip_file():
    print(shutil.make_archive('tf', 'zip', root_dir='./test_files'))


def unzip_file():
    print(shutil.unpack_archive('tf.zip', './unziped'))


def move_test():
    shutil.move('./unziped', './test_files/test1/test2')


target = os.path.join(os.getcwd(), "*")
final_result = []


def find_file(path, target):
    result = glob.glob(path)

    for data in result:
        if os.path.isdir(data):
            _path = os.path.join(data, '*')
            find_file(_path, target)
        else:
            if target in data:
                final_result.append(data)
    return final_result


final_result = []


def find_file_by_words(path, target):
    res = glob.glob(path)

    for data in res:
        if os.path.isdir(data):
            _path = os.path.join(data, '*')
            find_file_by_words(_path, target)
        else:
            try:
                f = open(data, 'r')
                content = f.read()
            except UnicodeDecodeError as e:
                print(f'data read failed {data}')
                f.close()
                continue
            if target in content:
                final_result.append(data)
            f.close()

    return final_result


data = {}


def clear(path):
    result = glob.glob(path)

    for _data in result:
        if os.path.isdir(_data):
            _path = os.path.join(_data, '*')
            clear(_path)
        else:
            name = os.path.split(_data)[-1]

            is_byte = False

            if 'zip' in name:
                is_byte = True
                f = open(_data, 'rb')
            else:
                f = open(_data, 'r', encoding='utf-8')
            content = f.read()
            f.close()

            if is_byte:
                hash_content_obj = hashlib.md5(content)
            else:
                hash_content_obj = hashlib.md5(content.encode('utf-8'))
            hash_content = hash_content_obj.hexdigest()

            if name in data:
                sub_data = data[name]

                is_delete = False

                for k, v in sub_data.items():
                    if v == hash_content:
                        glob.os.remove(_data)
                        print('%s will delete' % _data)
                        is_delete = True

                if not is_delete:
                    data[name][_data] = hash_content


            else:
                data[name] = {
                    _data: hash_content
                }


def update_names(path):
    result = glob.glob(path)
    for index, data in enumerate(result):
        if os.path.isdir(data):
            _path = os.path.join(data, "*")
            update_names(_path)
        else:
            path_list = os.path.split(data)
            name = path_list[-1]
            new_name = f'{index}_{name}'
            new_data = os.path.join(path_list[0], new_name)
            shutil.move(data, new_data)


if __name__ == '__main__':
    # copy_file()
    # move_file()
    # rm_file()
    # zip_file()
    # unzip_file()
    # move_test()
    # print(find_file(os.getcwd(), '.docx'))
    print(find_file_by_words(os.getcwd(), 'read'))
