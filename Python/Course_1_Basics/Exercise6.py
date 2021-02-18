num = 0
largest = -1
smallest = None
while True:
    num = input("ENTER A NUMBER: ")
    if num == 'done':
        break
    try:
         h = int(num)
    except :
        print("Invalid input")
    if largest < h:
        largest = h
        # print("h: max:", h, max)
    if smallest is None:
        smallest = h
    elif smallest > h:
        smallest = h
print('Maximum is', largest)
print('Minimum is', smallest)