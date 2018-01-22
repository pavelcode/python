# Author:pavel

#定义变量
name="张三"

print("我的名字叫",name)


name2 = name

print(name2,'---',name)


name ="李四"
print(name,"---",name2)


#定义常量
PI=3.1415926
print(PI)


#单行注释

"""
多行注释
"""

'''
多行注释
'''

#打印多行
msg ="""
我是李四
你是张三
"""
print(msg)


#获得用户输入
"""
username = input("你叫什么名字?")
print("你好,",username)
"""


#获得用户信息
name = input("你的名字")
age = input("你的年龄")
info=name+",今年"+age+"岁了"
print(info)


#获得用户信息
name = input("你的名字")
age = input("你的年龄")
info="""
{_name},今年{_age}岁了
""".format(_name=name,_age=age)
print(info)

"""
总结：不要用＋号连接运算符，
"""










