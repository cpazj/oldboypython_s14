#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: kent

age_of_zhaojian = 51

count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_zhaojian :
        print("Yes! You get it!")
        break
    elif guess_age > age_of_zhaojian:
        print("Please think smaller!")
    else :
        print("Please think bigger!")
    count +=1
else:
    print("You guess too times! fuck off!")