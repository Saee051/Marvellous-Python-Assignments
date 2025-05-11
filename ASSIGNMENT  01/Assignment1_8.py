#Write a program which accept number from user and print that number of '*' on screen

def PrintNo(no):
    for i in range(no):
        print("*")

print("Enter a number : ")
value = int(input())
PrintNo(value)        