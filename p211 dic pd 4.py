d1={"ram":33,"rahul":15,"devesh":30,"jayul":34,"jiya":16,"sadhana":11}


print(d1)
print("No\tMArks")
for k,v in d1.items():
    if v>20:
        print(k,"\t",v,"PAss")
    else:
        print(k,"\t",v,"fail")