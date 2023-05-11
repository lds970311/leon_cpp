from animal import lion_action
from animal import tiger_action
from animal.lion.action import Lion

"""
    清华：https://pypi.tuna.tsinghua.edu.cn/simple/

    阿里云：https://mirrors.aliyun.com/pypi/simple/

    中国科学大学 http://pypi.mirrors.ustc.edu.cn/simple/

    华中理工大学：http://pypi.hustunique.com/

    山东理工大学：http://pypi.sdutlinux.org/

    豆瓣：https://pypi.douban.com/simple/
    pip install -i https://pypi.douban.com/simple/ ipython

"""

if __name__ == '__main__':
    tiger_action.eat()
    lion_action.eat()
    lion = Lion()
    lion.sleep()
