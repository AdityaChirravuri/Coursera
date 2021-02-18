hrs = input("ENTER HOURS: ")
rate = input("ENTER RATE PER HOUR: ")
pay = float(hrs)*float(rate)
if float(hrs)>40 :
    hrs = float(hrs)-40
    pay = (float(40)*float(rate))  + (float(hrs)* float(rate)*1.5)
print(pay)