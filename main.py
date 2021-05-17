#!/usr/bin/env python
# -*- coding:utf-8 -*-
def my_fact(value_1):
    if value_1 == 1:
        return 1
    else:
        return value_1 * my_fact(value_1 - 1)
pass
pass
x = 1
while x == 1:
    value_1 = int(input("你可以输入你需要计算阶乘的value!\n"))
    answer = my_fact(value_1)
    print(value_1, "的阶乘是", answer)
    option = int(input('如果你要继续调试程序键入‘1’，任意键退出程序！\n'))
    if option != 1:
        x = 0