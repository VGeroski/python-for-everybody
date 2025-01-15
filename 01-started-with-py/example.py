def first_lesson():
    nam = input('Who are you? ')
    print('Welcome', nam)

def convert_elevator_floors():
    # Convert elevator floors
    inp = input('Europe floor? ')
    usf = int(inp) + 1
    print('US floor', usf)

def example_branching():
    x = 5
    print('Before 5')
    if (x == 5):
        print('Is 5')
        print('Is Still 5')
        print('Third 5')

    print('Afterwards 5')

def example_branching2():
    x = 5
    if (x > 2):
        print('Bigger than 2')
        print('Still bigger')

    print('Done with 2')

    for i in range(5):
        print(i)
        if (i > 2):
            print('Bigger than 2')
        print('Done with i', i)

    print('All Done')

def example_try_catch():
    # example try/catch
    astr = 'Hello Bob'
    try:
        # problematic conversion
        istr = int(astr)
    except:
        istr = -1

    print('First', istr)
    astr = '123'

    try:
        istr = int(astr)
    except:
        istr = -1

    print('Second', istr)

    # example try/catch
    rawstr = input('Enter a number: ')
    try:
        ival = int(rawstr)
    except:
        ival = -1

    if (ival > 0):
        print('Nice work')
    else:
        print('Not a number')

### Example 4.6
def computepay(h, r):
    pay = h * r
    if (h > 40):
        pay = h*r + (h - 40.0)*(r*0.5)
        
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fhrs = float(hrs)
frate = float(rate)

p = computepay(fhrs, frate)
print("Pay", p)

### End 4.6 example

### Example counting in a loop
count = 0
sum = 0
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)

print ('After', count, sum, sum/count)


found = False
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print ('After', found)

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if (smallest is None):
        smallest = value
    elif (value < smallest):
        smallest = value
    print(smallest, value)

print('After', smallest)

## Worked Exercise 5
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if (sval == 'done'):
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval

print('All Done')
print(tot, num, tot/num)

