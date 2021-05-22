#!/usr/bin/env python3
#-*- coding:utf-8 -*-   
print('这是一个用来完成基本运算的测试程序\n')
print("键入1是加法，键入2是减法，键入3是乘法，键入4是除法\n")
option=int(input('你现在可以选择运算模式了\n'))
num_1=int(input('键入第一个操作数\n'))
num_2=int(input('键入第二个操作数\n'))
if option==1:
    print('运算结果为',num_1+num_2)
elif option==2:
    print('运算结果为',num_1-num_2)
elif option==3:
    print('运算结果为',num_1*num_2)
elif option==4:
    print('运算结果的商为',num_1//num_2,'余数为',num_1%num_2)
else :
    print('非法的运算模式！\n')