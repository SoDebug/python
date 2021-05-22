#!/usr/bin/env python
#-*- coding:utf-8 -*-
def abs_pro(x):
    if x>=0:
        print("正数的绝对值为其本身！\n")
        pre_value=x
        new_value=x
        return pre_value,new_value
    else:
        print("负数的绝对值是它的相反数！\n")
        pre_value=x
        new_value=-x
        return pre_value,new_value
print("本程序是进阶版的绝对值求解函数，将会在函数返回值中返回两个函数！\n")
n=0
while n==0:
    value=int(input("请键入你需要测试的值，按下‘Enter'键完成输入\n"))
    value_1,value_2=abs_pro(value)
    print(value_1,"的绝对值为",value_2)
    option=int(input("你所测试已经完成，继续测试输入0，退出测试输入1\n"))
    if option==1:
        n=1
    elif option==0:
        n=0
    else:
        print("接收到了一个非正常的输入?请按照程序描述输入!\n")

