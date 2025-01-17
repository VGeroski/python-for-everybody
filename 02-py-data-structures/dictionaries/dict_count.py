### Counts words from text file

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)

for key in counts:
    print(key, counts[key])
