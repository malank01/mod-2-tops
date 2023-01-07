#Write a Python program to sum of three given integers. However, if
#two values are equal sum will be zero

a=int(input("enter number : "))
b=int(input("enter number : "))
c=int(input("enter number : "))

if a==b or a==c or b==c :
    sum=0
    print("sum is zero",0)

else:
    print("sum of a,b,c : ",a+b+c)
