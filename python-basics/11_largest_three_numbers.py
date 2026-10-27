a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the largest number")
elif b >= a and b >= c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")
