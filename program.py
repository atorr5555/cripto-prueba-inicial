import fileinput

total = 0
for line in fileinput.input():
	total += float(line)

if total.is_integer():
	total = int(total)
print(total)