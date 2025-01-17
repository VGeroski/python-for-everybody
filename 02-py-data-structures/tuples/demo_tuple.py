d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

d = {'a':10, 'c':22, 'b':1}
print(sorted(d.items()))

for (k, v) in sorted(d.items()):
    print(k, v)

# Sort by Values
tmp = list()
for (k, v) in d.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True) # sorting will be done by keys, but keys are now previous values
print(tmp)
