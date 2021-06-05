#!usr/bin/env python
#-*- coding:utf-8 -*-
class student(object):
    def __init__ (self,name,id,score):
        self.__name=name
        self.__id=id
        self.__score=score
    def print_message(self):
        print("%s的身份id为%s\n成绩为%s"%(self.__name,self.__id,self.__score))
    def set_score(self,score):
        self.__score=score
    def print_grade(self):
        if self.__score>=60 and self.__score<80:
            return 'C'
        elif self.__score>=90:
            return 'A'
        elif self.__score>=80 and self.__score<90:
            return 'B'
        else:
            return 'D'
张三=student('张三',1,88)
李四=student('李四',2,98)
张三.print_message()
print('获得评价',张三.print_grade())
李四.print_message()
print('获得评价',李四.print_grade())
张三.set_score(100)
张三.print_message()
print('获得评价',张三.print_grade())
李四.set_score(60)
李四.print_message()
