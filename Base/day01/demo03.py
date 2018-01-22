#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Author:pavel


#while语句
while True:
    age = int(input("猜下我的芳龄"))
    if age==20:
     print("你猜对了,记得买彩票")
     break
    elif age>20:
     print("我有那么老吗！！！")
    else:
     print("岁月已逝，芳华犹在")

