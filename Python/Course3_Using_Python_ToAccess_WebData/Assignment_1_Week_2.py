import re
handle = open("Assignment.txt")
#print(handle)
x = list()
for line in handle:
    y = re.findall('[0-9]+', line)
    x  = x + y

s = 0
for z in x :
    s = s+ int(z)

print(s)
