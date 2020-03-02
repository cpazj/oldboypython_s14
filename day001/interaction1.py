#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kent
#演示input交互以及格式化输出

name = input("name:")
age = int(input("age:")) #强制转换输入的内容为整形 integer
print("type of age:",type(age))
job = input("job:")
salary = input("salary:")

info1 = '''
---------------info of %s--------------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' %(name,name,age,job,salary)

print(info1)

#info2 推荐的写法
info2 = '''                         
---------------info of {_name}--------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name,             #注意这里format前面的'.'
           _age=age,
           _job=job,
           _salary=salary)

print(info2)

info3 = '''                         
---------------info of {0}--------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(name,age,job,salary)

print(info3)