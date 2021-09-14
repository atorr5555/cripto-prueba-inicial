import fileinput

total = 0
for line in fileinput.input():
	total += float(line)

print(total)