a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swap: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swap: a =", a, "b =", b)

