import csv

students = []
with open('students.csv', "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        for str in row:
            str1 = str.split(";")
            students.append((str1[0], str1[2]))

old = 9999
young = 0
bigboy = ''
smallboy = ''
for student in students:
    if int(student[1][1:5]) > young:
        young = int(student[1][1:5])
        smallboy = student[0]
    if int(student[1][1:5]) < old:
        old = int(student[1][1:5])
        bigboy = student[0]

with open('result.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([bigboy + " самый старый", smallboy + " молоденький"])

print(bigboy, smallboy)