#Write a Python function that takes a list of words and returns the length of the longest one

l=["top","technology","python","java","djangoj"]
a=len(l[0])
for i in l:
    if len(i)>a:
        a=len(i)
        b=i

print("Longest Word : ",b)



