text = "X-DSPAM-Confidence:    0.8475"
index=text.find('0')
abc = text[index: ]
x=float(abc)
print x