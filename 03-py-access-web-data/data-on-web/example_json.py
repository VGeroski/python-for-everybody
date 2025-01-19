import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

json_data = json.loads(data)
comments = json_data["comments"]

nums = list()
for comment in comments:
    nums.append(int(comment["count"]))

print('Count:', len(nums))
print('Sum:', sum(nums))
