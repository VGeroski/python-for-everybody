import sqlite3

conn = sqlite3.connect('databases/test.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'

fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: '): continue

    pieces = line.split()
    email = pieces[1]
    email_parts = email.split('@')
    host = email_parts[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (host,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (host,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (host,))

    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
