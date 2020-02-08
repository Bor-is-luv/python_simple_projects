import csv

laptops = []
with open('laptops.csv', "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        for str in row:
            str1 = str.split(";")
            laptops.append((str1[0], str1[2]))

print(laptops)
lot = int(laptops[0][1]) - 1
few = int(laptops[0][1]) + 1
expensive = ''
cheap = ''
for laptop in laptops:
    if int(laptop[1][1:5]) > lot:
        lot = int(laptop[1][1:5])
        expensive = laptop[0]
    if int(laptop[1][1:5]) < few:
        few = int(laptop[1][1:5])
        cheap = laptop[0]

with open('result.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([cheap + " дёшево", expensive + " на степуху не купишь"])

print(expensive, cheap)