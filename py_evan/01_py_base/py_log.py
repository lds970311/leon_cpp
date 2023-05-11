# coding:utf-8
# time: 2023/5/11
# author: evan
# python中的日志

import logging
import os


def init_log(path):
    mode = ''
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(filename)s    [line:%(lineno)s]   %(levelname)s   %(message)s",
        filename=path,
        filemode=mode
    )
    return logging


if __name__ == '__main__':
    log = init_log('./logs/my.log')
    log.info('hello logger')
    log.debug("debug")
    log.warning('warning')
    log.error('error')
    log.critical('critical')
