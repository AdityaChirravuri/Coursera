fh = open('Assignment_8.5.txt')
#print(fh)
lst = list()
t = list()
counts = dict()
for line in fh:
    if line.startswith('From'):
        words = line.split()
        t.append(words[1])

for j in range(len(t)):
    if 2*j +1 <len(t):
        lst.append(t[2*j+1])
        
for word in lst:
    counts[word]= counts.get(word, 0)+1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


