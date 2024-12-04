row1 = ["😀", "😀", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
# column, row

column_index = int(position[0]) - 1
row_index = int(position[1]) - 1
print(column_index)
print(row_index)
map[row_index][column_index] = 'x'

# print(map)
print(f"{row1}\n{row2}\n{row3}")

