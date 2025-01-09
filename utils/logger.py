#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import logging
import os
import time


class Logger:
    def __init__(self, loggername):
        # 创建一个logger
        self.logger = logging.getLogger(loggername)
        print(self.logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入文件
        rq = time.strftime('%Y%m%d %H-%M-%S', time.localtime(time.time()))
        log_path = os.path.abspath('.') + '/logs/'  # 指定文件输出路径，注意logs是一个文件夹，
        logname = log_path + rq + 'test.log'  # 指定输出的日志文件名
        fh = logging.FileHandler(logname, encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        print(fh)
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger