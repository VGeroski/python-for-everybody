abc = 'With three words'
stuff = abc.split() #default is split on white space
print(stuff)

line = 'first;second;third'
thing = line.split(';')
print(thing)

# Find email from messages in email box
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()
    email = words[1]
    print('Email:', email) # email

    pieces = email.split('@')
    print('Host:', pieces[1])
   
