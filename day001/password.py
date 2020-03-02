#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kent

#改程序需要在终端环境下运行，pycharm下不能得到正确结果
import getpass
username = input("username:")
passoword = getpass.getpass("passorod:")

print(username,passoword)