import os

input = raw_input("ENTER THE DIRECTORY PATH : ")

list = os.listdir(input)
os.chdir(input)
for item in range(len(list)):
	print list[item]+"	"+str(os.stat(os.path.abspath(list[item]))[1])
