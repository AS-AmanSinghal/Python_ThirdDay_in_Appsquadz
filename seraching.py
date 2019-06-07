a=[]
n=int(input("Enter range"))
for i in range(0,n):
    b=int(input())
    a.append(b)

count=0
print("Enter element for searching ")
c=int(input())
for i in range(0,len(a)):
    if a[i]==c:
        count=1
        break

if count==0:
    print("no")
else:
    print("yes")