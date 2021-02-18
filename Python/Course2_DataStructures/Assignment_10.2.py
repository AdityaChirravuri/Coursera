handle = open('Assignment_8.5.txt')
#print(handle)
hcount = dict()
hlst = list()
for lines in handle:
    words = lines.split()
    if lines.startswith('From') and len(words) > 2:
        hr = words[5].split(':')
        hcount[hr[0]] = hcount.get(hr[0], 0)+1
    else : continue


for k, v in hcount.items():
    hlst.append((k, v))

hlst.sort()
for k, v in hlst:
    print (k, v)
