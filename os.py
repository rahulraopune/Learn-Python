import os

input = raw_input("Enter the path : ")

stattuple =  os.stat(input)

print "inode of %s is %d" % (input,stattuple[1])
