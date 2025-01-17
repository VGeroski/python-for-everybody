fhand = open('mbox.txt')

count = 0
for line in fhand:
    count = count + 1
    
    # strip white space at the end \n
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

print('Line Count:', count)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)
