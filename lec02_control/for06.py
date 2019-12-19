"""
dictionary comprehension
"""

numbers = [1,2,3,4,5]
names = ['a','b','c','d','e']

students = {} # 비어있는 dictionary
for i in range(len(names)):
    students[numbers[i]] = names[i] # dictionary 생성
print(students)

students2 = {numbers[i] : names[i] for i in range(len(numbers))}
print(students2) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

num_name = zip(numbers, names)
print(num_name)
for x in zip(numbers, names):
    print(x)

students3 = {}
for key,value in zip(numbers, names):
    students3[key] = value
print(students3)

students4 = {k: v for k, v in zip(numbers, names)}
print(students4)

students5 = {k: v for k, v in zip(numbers, names) if k % 2}
print(students5)
