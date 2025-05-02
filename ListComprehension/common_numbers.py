

with open("file1.txt") as file1:
    file1_numbers = file1.readlines()
    list_1 = [int(num) for num in file1_numbers]

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()
    list_2 = [int(num) for num in file2_numbers]

# Solution using for loop
# result = []
# for num in list_1:
#     if num in list_2:
#        result.append(num)
#
# print(result)  # [3, 6, 13, 5, 7, 12, 33, 42]

# Solution using list comprehension
result = [num for num in list_1 if num in list_2]
print(result) # [3, 6, 5, 33, 12, 7, 42, 13]