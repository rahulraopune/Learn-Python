a = 0
b = 1

r = raw_input("ENTER THE RANGE : ")
print str(a)+"\n"
print str(b)+"\n"
sum = 0  
for i in range(2,int(r)):
	sum = a + b
	print str(sum)+"\n"
	a = b
	b = sum
