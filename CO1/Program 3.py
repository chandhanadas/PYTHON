list=[-5,18,0,14,-18,17]
print(list)
newlist=[x for x in list if x>0]
print("the positive numbers are:",newlist)

_____________________________________________________________
num=[]
n=int(input("enter a number:"))
for i in range(n):
    num.append(int(input("enter the number to insert:")))
result=[x*x for x in num]
print(result)

______________________________________________________________
n=input("enter your name:")
k=list(n)
b=[x for x in k if "a" in x or "e" in x or "i" in x or "o" in x or "u" in x]
print(len(b))
print(b)

__________________________________________________________________________________
w=input("enter a word:")
ord=[ord(x) for x in w]
print("the ordinal value is:",ord)
