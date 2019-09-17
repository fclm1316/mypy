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

print('=========================')

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    # 重写父类
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def eat(self):
        print('Cat is eating')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

def run_twice(some):
    some.run()
    some.run()

print('+++++++++++++++')
run_twice(Animal())

run_twice(Dog())

class Bat(Animal):
    def run(self):
        print('bat is running')

run_twice(Bat())
