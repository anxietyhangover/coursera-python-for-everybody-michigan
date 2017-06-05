name = raw_input("Enter file:")
fh = open(name)
y=dict()
k=list()
for line in fh:
    words=line.split()
    for word in words:
         x=words[0]
         if x=="From":
                k.append(words[1])
                break
for l in k:
    y[l]=y.get(l,0)+1
m=1
m1=0
for m in y:
    if y[m] > m1:
        f=m
        m1=y[m]
print f,y[f]

                
