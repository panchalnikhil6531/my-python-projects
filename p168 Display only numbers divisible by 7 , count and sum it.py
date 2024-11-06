tupleD=(7,14,24,67,54,99,87,12,56)
s=0
c=0
for x in tupleD:
        if x % 7 == 0:
            print(x)
            s=s+x
            c=c+1

print("sum =>",s )
print("count =>",c)