import re

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    # with ^ -> same as line.startswith('From:')
    if re.search('^From:', line):
        email = re.findall('From: (\S+@\S+)', line)
        print('Email:', email[0])
        host = re.findall('@([^ ]*)', line)
        print('Host:', host[0])
        
