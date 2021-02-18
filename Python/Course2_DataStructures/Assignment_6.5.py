# find and slicing the string

text = "X-DSPAM-Confidence:    0.8475";
print(text)
ipos = text.find(':')
print(ipos)
piece = (text[ipos+5:])
print(piece)
head = float(piece)
print(head)

