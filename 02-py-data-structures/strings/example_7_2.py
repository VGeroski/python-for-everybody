# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(':')
    sval = line[ipos+1:]
    fval = float(sval.strip())
    total = total + fval
    count = count + 1

print("Average spam confidence:", total/count)
