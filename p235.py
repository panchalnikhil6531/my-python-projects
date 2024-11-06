def add():
    a=int(input("enter  a=>"))
    b=int(input("enter b=>"))
    print("add=",a+b)
def max2():
    a = int(input("enter  a"))
    b = int(input("enter b"))
    if a>b:
        print("no 1 is big ")
    else:
        print("no2 is big ")
add()
max2()

def max3():
    a = int(input("enter  a=>"))
    b = int(input("enter b=>"))
    c=int(input("enter c =>"))
    if a > b and a>c:
        print("no 1 is big ")
    if b>a and b>c:
        print("no2 is big ")
    if c>a and c>b:
        print("no3 is big ")
add()
max3()
def odd ():
    a=int(input("enter a =>"))
    if a%2==0:
        print("number is even ")
    else:
        print("number is odd")
odd()

def table():
    n =int(input("enter n =>"))
    for i in range(1, 11):
        print(n, " X ", i, " = ", n * i)




table()

def area():
    h = float(input("enter value of height => "))
    b = float(input("enter value of base =>"))
    area = h * b * 0.5
    print("Area of triangle = ", area)


area()

def circle ():
    r = int(input("enter r =>"))
    area = r * r * 3.14
    print("Area of circle = ", area)

circle()

def cube ():
    n = int(input("Enter the number: "))
    s = 0
    for i in range(1, n + 1):
        cube = i * 3
        print(cube)
cube()

def positiv():
    numbers = int(input("enter number="))
    if numbers > 10:
        print("number is positive")
    else:
        print("number is negetive")
positiv()
