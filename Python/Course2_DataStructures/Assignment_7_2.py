line = open('Assignment_7.2.txt')
count = 0
sum = 0.0
for i in line:
    if not i.startswith("X-DSPAM-Confidence:"):continue
    count = count+ 1;
    #print(i)
    pos = i.find(':')
    val = i[pos+2:]
    val.strip()
    value = float(val)
    sum = sum + value
    #print(value, sum)
    
avg = sum/count
print("Average spam confidence:", avg)
