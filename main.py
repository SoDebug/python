#!usr/bin/env python
#-*- coding:utf-8 -*-
class people(object):
    def __init__(self,name,sex,id):
        self.__name=name
        self.__sex=sex
        self.__id=id
    def check(self):
        print('%s的性别是%s,id是%s'%(self.__name,self.__sex,self.__id))
    def loading(self):
        print("正在加载中，请稍等...\n")
class student(people):
    def __init__(self,grade,classes):
        self.__grade=grade
        self.__classes=classes
    def check_student(self):
        print("成绩为%s,班级为%s"%(self.__grade,self.__classes))
class teacher(people):
    def __init__(self,classes):
        self.__classes=classes
    def check_teacher(self):
        print("班级为%s"%(self.__classes))
#类与方法编写完毕，方法完成继承
#开始创造对象
张三=people("张三","XY",20210601)
张三.check()
张三=student(98,1)
张三.check_student()
李红老师=people("李红老师","XX",202114)
李红老师.check()
李红老师=teacher(1)
李红老师.check_teacher
#继承的是方法
