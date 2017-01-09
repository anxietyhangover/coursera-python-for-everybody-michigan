fname = raw_input("Enter file name: ")
fh = open(fname)
x=list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        y=word in x
        if y==False:
    		x.append(word)        
x.sort()
print x
