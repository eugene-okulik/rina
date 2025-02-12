"""Create a dictionary with the following keys ‘tuple’, ‘list’, ‘dict’, ‘set’"""
my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [1, 2, 3, 4, 5],
    "dict": {"one": "value1", "two": "value2", "three": "value3",
             "four": "value4", "five": "value5"},
    "set": {1, 2, 3, 4, 5}
}
print(my_dict["tuple"][-1])  # The last element was printed
my_dict["list"].append(6)  # An element is added to the end of the list
my_dict["list"].pop(1)  # The second element of the list was deleted
print(my_dict["list"])
my_dict['dict'][("i am a tuple",)] = (10, 20, 30, 40, 50)  # An element is added
my_dict["dict"].pop("three")  # The element with the key "three" of the dict was deleted
print(my_dict["dict"])
my_dict["set"].add(10)  # An element is added
my_dict["set"].discard(2)  # The element "two" was deleted
print(my_dict["set"])
print(my_dict)
