
fname = raw_input("Enter file name: ")
fh = open(fname)
x=0
y=list()
for line in fh:
    words=line.split()
    for word in words:
    	y=words[0]
    	if y=="From":
        	print words[1]
        	x=x+1
            break
print "There were",x,"lines in the file with From as the first word"
