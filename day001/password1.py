
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kent

#改程序需要在终端环境下运行，pycharm下不能得到正确结果
import getpass
_username = 'zhaojian'
_password = 'abc123'

username = input("username:")
#password = getpass.getpass("password:")
passoword = input("passorod:")

if _username == username and _password == passoword:
    print("Welcome user {name} login~~~~".format(name = username))
else:
    print("Invalid username or password!")
