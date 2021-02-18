h = input("ENTER HOURS: ")
r = input("ENTER RATE PER HOUR: ")
def computepay(h, r):
    pay = (float(h) * float(r))
    if float(h) > 40:
        hrs = float(h) - 40
        pay = (float(40) * float(r)) + (float(hrs) * float(r) * 1.5)
        return pay
print(computepay(h, r))