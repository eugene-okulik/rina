"""given the cathetuses of a right triangle. find its hypotenuse and area"""
import math
cathetus_1 = float(input("insert cathetus_1"))
cathetus_2 = float(input("insert cathetus_2"))
hypotenuse = math.sqrt(cathetus_1 ** 2 + cathetus_2 ** 2)
area = cathetus_1 * cathetus_2 / 2
print(hypotenuse)
print(area)
