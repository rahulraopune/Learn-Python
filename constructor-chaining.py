class A:
	def __init__(self):
		print "constructor A"

class B(A):
        def __init__(self):
		A.__init__(self) #constructor not called by default
                print "constructor B"

b = B()
