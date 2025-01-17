print('Exercise 6.5')

string = 'X-DSPAM-Confidence: 0.8475'

ipos = string.find(':')
print(ipos)

piece = string[ipos+1:]
value = float(piece)

print(value)
