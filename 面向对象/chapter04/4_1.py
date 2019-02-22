#!/usr/bin/python3
#coding:utf-8
class Cat(object):
    def say(self):
        print('i am a cat')

class Dog(object):
    def say(self):
        print('i am a dog')

class Duck(object):
    def say(self):
        print('i am a duck')

animal = Cat()
animal.say()
#
#list 中可以指向任何一个类，他们拥有共同的say()方法，多态。
#java 中要重写say()方法
animal_list = [Cat,Dog,Duck]
for animal in animal_list:
    #同时调用say()方法
    animal().say()

