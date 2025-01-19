import re

hand = open('test2.txt')
total = 0
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) <= 0: continue
    for num in numbers:
        total = total + int(num)

print('Sum is:', total)
