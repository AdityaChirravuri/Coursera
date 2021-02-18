score = input("ENTER SCORE: ")
s = float(score)
if s>1:
    print("ENTER LESS THAN OR EQUAL 1 ")
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.6:
    print("F")
elif s<0:
    print("ENTER VALID SCORE")