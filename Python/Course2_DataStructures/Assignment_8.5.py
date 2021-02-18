fh = open('Assignment_8.5.txt')
#print(fh)
lst = list()
t = list()
count = 0
for i in fh:
    #print(i)
    if i.startswith('From'):
        lst = i.split()
        t.append(lst[1])

for j in range(len(t)):
    if 2*j+1 < len(t):
        print(t[2*j+1])
count = len(t)/2
print("There were", int(count), "lines in the file with From as the first word")
