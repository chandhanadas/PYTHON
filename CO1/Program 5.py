n=int(input("entr no of list elements:"))
over=[]
for i in range(n):
    over.append(int(input("entr element:")))
    if over[i]>100:
        over[i]="over"
print(over)
