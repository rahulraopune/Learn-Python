class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class LinkedList:
    def __init__(self):
	self.first=None
	self.new1=None   	     
	self.current=None

    def insert(self,data):
    	if self.first == None:
            self.new1 = Node(data)
            self.new1.data = data
            self.first = self.new1
            self.current = self.new1
        else:
            self.new1 = Node(data)
            self.new1.data = data
            self.current.right=self.new1
            self.new1.left=self.current
            self.current = self.new1

        
    def __str__(self):
	strvar = ""
        p = self.first
        while p!=None:
            strvar += str(p.data)+" "
            p = p.right
	return strvar

if __name__ == "__main__":
    l = LinkedList()
    for i in xrange(50):
        l.insert(random(i))	
    print l
