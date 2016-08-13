list = [1,3,7,8,77]

def search(list,key,low,high):
	if(low>high):
		return "element not found"
	
	mid = int((low+high)/2)

	if(list[mid]==key): 
		return mid
	elif (list[mid]<key):
		return search(list,key,mid+1,high)
	else:
		return search(list,key,low,mid-1)	
	



print search(list,77,0,len(list))
