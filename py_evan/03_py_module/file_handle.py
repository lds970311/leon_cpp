# coding:utf-8
# time: 2023/5/11
# author: evan
# python文件操作
import os


def create_py_package(path):
    if os.path.exists(path):
        raise Exception(f'{path} 已经存在')

    os.makedirs(path)
    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write('# coding:utf-8\n')
    f.close()


class Open(object):
    def __init__(self, path, mode='w', is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode)
        if self.is_return:
            message = '%s\n' % message
        f.write(message)
        f.close()

    def read(self, is_strip=True):
        result = []
        with open(self.path, self.mode) as f:
            data = f.readlines()
        for line in data:
            if is_strip:
                temp = line.strip()
                if temp != "":
                    result.append(temp)
            else:
                if line != '':
                    result.append(line)
        return result


def copy_file(src: str, dest: str) -> None:
    if src or dest is None:
        return
    """
    文件复制
    :param src: 原路径 
    :param dest: 目标路径
    :return: None
    """
    with open(src, 'rb') as src_file, open(dest, 'wb') as dst_file:
        # 逐块读取源文件数据，并将数据写入目标文件
        while True:
            data = src_file.read(1024)
            if not data:
                break
            dst_file.write(data)


if __name__ == '__main__':
    current_path = os.getcwd()
    file_path = current_path + '/TestFiles/a.txt'
    # create_py_package(current_path + '/TestFiles/test')

    # open = Open(file_path, 'rb')
    # result = open.read()
    # print(result)
    #
    with open(file_path, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            print(line.decode('utf8'))

    src = '/home/lds/Pictures/犬夜叉 桔梗 夕阳背景 巫女服 彼岸花 回眸 4k动漫壁纸_彼岸图网.jpg'
    dest = './test.jpg'
    copy_file(src, dest)
