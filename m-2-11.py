#Write a python program to sum of the first n positive integers

n=int(input("enter num : "))
sum=0
while n>0:
    sum=sum+n
    n=n-1
    print("sum",sum)
