import fileinput

total = 0
for line in fileinput.input():
	total += line

print(total)