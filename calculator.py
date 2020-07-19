# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:48:01 2019

@author: SELVAKUMAR
"""

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("select operation")
print("1.add\n 2.subtract\n 3.multiply\n 4.divide\n")

choice=input("enter the choice")
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))

if choice == '1':
    print(n1,"+",n2,"=",add(n1,n2))
elif choice == '2':
    print(n1,"-",n2,"=",sub(n1,n2))
elif choice == '3':
    print(n1,"*",n2,"=",mul(n1,n2))
elif choice == '4':
    print(n1,"/",n2,"=",div(n1,n2))
else:
    print("invalid input entered")