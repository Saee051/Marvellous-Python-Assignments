#write the program which contains one functions named as ChkNum() which accept one parameter as number.

def ChkNum(no):
    no = 0
    print("Enter number:")
    no = int(input())

    if  no %2:
        print("Odd number")
    else:
        print("Even number")

i = 0
value = ChkNum(i)            