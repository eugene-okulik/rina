"""This script demonstrates string parsing, formatting, and list operations in Python."""
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Исходные строки с результатами
text = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]
result1 = text[0]
index1 = result1.index(':') + 1
number = int(result1[index1:])
print(number + 10)
result2 = text[1]
index2 = result2.index(':') + 1
number2 = int(result2[index2:])
print(number2 + 10)
result3 = text[2]
index3 = result3.index(':') + 1
number3 = int(result3[index3:])
print(number3 + 10)
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print("Students", ", ".join(students), "study these subjects:", ", ".join(subjects))
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ", ".join(students)
subjects = ", ".join(subjects)
print("Students {0}, study these subjects:{1}".format(students, subjects))
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ", ".join(students)
subjects = ", ".join(subjects)
print(f"Students {students}, study these subjects: {subjects}")
