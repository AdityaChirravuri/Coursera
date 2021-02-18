fh = open('Assignment_8.4.txt')
lst = list()
b = list()
for l in fh:
    line = l.rstrip()
    a = line.split()
    b = b + a
    #print(b)
#print("Total list is: ", b)
b.sort()
#print(b)
z = len(b)
for i in range(z):
    if i < z-1 and b[i] != b[i+1]:
        lst.append(b[i])
    #print(lst)
lst.append(b[z-1])
print(lst)
    
