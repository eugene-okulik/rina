"""x and y are given, get the result of x − y / 1 + xy"""
x = float(input("insert x: "))
y = float(input("insert y: "))
result = (x - y) / (1 + x * y)
print(result)
