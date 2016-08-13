import sys

def inttobin32inverse(num):
	revbin = ''
	while num!=0:
		revbin += str(num%2)
		num /= 2
	
	smallbin=''
	for i in range(len(revbin)):
		smallbin += revbin[len(revbin)-1-i]
	
	remlen = 32 - len(smallbin)
	
	zerostr=''
	for i in range(remlen):
		zerostr += '0'

	bin32 = zerostr + smallbin

	#print "original "+bin32
	bin32inverse = []

	for i in range(len(bin32)):
		if bin32[i]=='0':
			bin32inverse.append(1)
		else:
			bin32inverse.append(0)
	#print "Inverse "+str(bin32inverse)
	return bin32inverse
	
def valueofbin32inverse(listvar):
	sum=0
	for i in range(len(listvar)):
		sum += listvar[len(listvar)-1-i]*(2**i)
	return sum	
	
if __name__=="__main__":
	t = int(raw_input())
	while t>0:
		l = inttobin32inverse(4)
		print valueofbin32inverse(l)
		t--
	
