fname = raw_input("Enter file name: ")
y=0.0
i=0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        b=line.index('0')
        index2=b+6
        x=line[b:index2]
        z=float(x)
        y=y+z
        i=i+1
avg=y/i
print "Average spam confidence:",avg
