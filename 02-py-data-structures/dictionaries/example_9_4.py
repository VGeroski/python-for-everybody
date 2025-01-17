name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1
        
max_num_emails = None
max_email = None
for email, count in counts.items():
    if max_num_emails is None or count > max_num_emails:
        max_num_emails = count
        max_email = email

print(max_email, max_num_emails)
