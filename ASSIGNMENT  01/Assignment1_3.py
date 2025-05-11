#Write a program which contains one function named as Add() which accepts two nos from user and return addition of that two numbers.

def Add(value1, value2):
    ans = 0

    ans = int(value1) + int(value2)

    print("Addition is : ",ans)

print("Enter the First number : ")
no1 = int(input())

print("Enter the second number : ")
no2 = int(input())

Add(no1,no2)