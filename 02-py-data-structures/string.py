fruit = 'banana'
w = fruit[2]
print(w)

# how long is string
print(len(fruit))

index = 0
while index < len(fruit):
    x = fruit[index]
    print(index, x)
    index = index + 1

for letter in fruit:
    print(letter)

# count a in banana
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print('there is',count, 'times a in banana')


# Slicing Strings
s = 'Monty Python'
print(s[0:4]) # up to but not including
print(s[6:7])
print(s[6:20]) # not traceback, it will go to the end
print(s[:2]) # same as [0:2]
print(s[8:]) # from 8 to the end
print(s[:]) # print whole string

# String Manipulation
a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

# 'n' in fruit => True
# 'nan' in fruit => True

if 'a' in fruit:
    print('Found it!')

pos = fruit.find('na')
print(pos)

print(fruit.upper())

nstr = fruit.replace('a', 'AA')
print(nstr)

tmp = '   Text   '
print(tmp.lstrip() + 'a')
print(tmp.rstrip() + 'a')
print(tmp.strip() + 'a')

line = 'Please have a nice day'
if (line.startswith('Please')):
    print('Good line')

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# print host from email

atpos = data.find('@')
sppos = data.find(' ', atpos) # we search for space position, but from at position, not from begging

host = data[atpos + 1 : sppos]
print('Host:', host)
