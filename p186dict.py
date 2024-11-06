import random
d1={}
n=int(input("Enter limit =?"))

for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v

print(d1)
print("No\tMArks")
print("*"*20)
for k,v in d1.items():
        print(k,"\t",v,"PAss")
print("*"*20)