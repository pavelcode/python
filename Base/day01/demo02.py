#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Author:pavel



#if语句
username = input("请输入用户名:")
userpass = input("请输入密码:")
if username=="admin" and userpass=="123":  #注意 用冒号
  print("登陆成功")      #注意缩进
else:
  print("用户名或密码失败")



#if elif语句
age = int(input("猜下我的芳龄"))
if age==20:
 print("你猜对了,记得买彩票")
elif age>20:
 print("我有那么老吗！！！")
else:
 print("岁月已逝，芳华犹在")

