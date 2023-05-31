file = open("numbers.txt", "r")
lines = file.readlines()
sum = 0
for index, line in enumerate(lines):
    sum += int(line)

print(sum)
file.close()
