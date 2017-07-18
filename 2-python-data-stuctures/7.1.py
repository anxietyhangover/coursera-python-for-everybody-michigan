# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for x in fh:
    x=x.rstrip()
    print x.upper()

