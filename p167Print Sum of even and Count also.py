tupleD=(1,435,676,878,96,3,2,5,8,0,23,45)
c=0
for x in tupleD:
        if x % 2 == 0:
            print(x)
            c=c+1

print("count =",c )