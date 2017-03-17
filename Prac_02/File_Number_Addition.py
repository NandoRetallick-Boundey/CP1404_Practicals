in_file = open("numbers.txt", mode='r')

total = 0

for line in in_file:
    total += int(line)
print(total)
