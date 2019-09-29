a=[]
n=int(input("enter no"))
for i in range(0,n):
       num=int(input("enter number"))
       a.insert(i,num)
print(a)
a[3]=a[5]
a[len(a)-1]=a[5]
a.append(a[5])
del a[5]
print(a)
