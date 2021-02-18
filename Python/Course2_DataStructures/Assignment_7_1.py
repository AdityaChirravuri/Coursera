#print("hi")
fh = open('Assignment_7.1.txt')
print(fh)

for x in fh:
    ly = x.rstrip()
    print(ly.upper())
