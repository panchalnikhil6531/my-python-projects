import time
current=time.localtime(time.time())
h=current.tm_hour
if h<12:
    print("good morning")
if h>12 and h<18:
    print("good evening ")
else:
    print("good night")
