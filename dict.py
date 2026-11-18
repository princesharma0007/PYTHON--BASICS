# student = {
#     "name": "Prince",
#     "age": 20,
#     "marks": 85
# }

# print(student["name"])       # Prince
# print(student.get("age"))    # 20
# print(student.get("height", 0))  # 0 (default value if key is not found)
# student.update({"marks": 90, "height": 5.9})  # Update marks and add height
# # print(student)  # {'name': 'Prince', 'age': 20, 'marks': 90, 'height': 5.9}
# del student["age"]  # Remove the age key-value pair
# print(student)  # {'name': 'Prince', 'marks': 90, 'height': 5.9}
# student.pop("marks")  # Remove and return the value of the marks key
# print(student)  # {'name': 'Prince', 'height': 5.9}
# new_student = student.popitem()  # Remove and return an arbitrary key-value pair
# print(new_student)  # ('name', 'Prince') or ('height', 5.9) depending on the internal order of the dictionary
# print(student)  # Remaining key-value pairs
# student.clear()  # Remove all key-value pairs 




# dictionary=dict(name="Prince", age=20, marks=85)

# # print(dictionary)

# keys = ["a", "b", "c"]

# d = dict.fromkeys(keys, None)

# print(d)

teacher = {
    "name": "ladle",
    "[]": "meow",
    "experience": 10
}
print(teacher.keys())    # dict_keys(['name', 'subject', 'experience'])
print(teacher.values())  # dict_values(['ladle', 'Meow', 10])
print(teacher.items())   # dict_items([('name', 'ladle'), ('subject', 'Meow'), ('experience', 10)])
# for value in teacher.items():
#     print(value)

string=str(teacher)
print(string)
print(type(string))  # <class 'str'>
# teacher.sort()  # This will raise an AttributeError since dictionaries do not have a sort method
# print(teacher)  # Output: {'name': 'ladle', 'subject': 'Meow', 'experience': 10}
print(any(teacher))  # True
print(all(teacher))  # True
print(max(teacher))  # 'subject' (based on lexicographical order of keys)
print(min(teacher))  # 'experience' (based on lexicographical order of keys)
