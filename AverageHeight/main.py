
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sumOfHeight = 0;
count = 0;
for height in student_heights:
    count += 1;
    sumOfHeight += height;

average_height = round(sumOfHeight / count);

print(average_height)

print (round(sum(student_heights) / len(student_heights)))

