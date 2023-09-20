# import random
# numbers1 = []
# for _ in range(10):
#     numbers1.append(random.randint(-10, 10))
#
# print(numbers1)
#
# numbers2 = []
#
# for number in numbers1:
#     if number % 2 ==0:
#         numbers2.append(number)
#
# print(numbers2)
#
# numbers2 = []
#
# for number in numbers1:
#     if number % 2 != 0:
#         numbers2.append(number)
#
# print(numbers2)
#
# numbers2 = []
#
# for number in numbers1:
#     if number >= 0:
#         numbers2.append(number)
#
# print(numbers2)

#######
import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# result = 0
# for i in range(len(numbers)):
#     if i % 3 != 0:
#         print(i, end =" ")
#         result == numbers[i]
#
#     print(result)

result = 0
min_value = min(numbers)
max_value = max(numbers)
min_value_index = numbers.index(min_value)
max_value_index = numbers.index(max_value)
print(min_value)
print(max_value)
print(min_value_index)
print(max_value_index)


if min_value_index > max_value_index:
    min_value_index, max_value_index = max_value_index, min_value_index


for i in range(min_value_index + 1, max_value_index):
    result += numbers[i]

print ()

result = 0

first_positive_index = 0
last_positive_index = 0

for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive_index = 1
        break


for i in range(len(numbers) -1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = 1
        break

print(first_positive_index)
print(last_positive_index)