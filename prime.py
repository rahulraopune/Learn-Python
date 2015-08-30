r = raw_input("Enter the range : ")
for num in range(1,int(r)):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print num
