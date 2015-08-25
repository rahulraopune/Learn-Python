class Student:
	
	studentcount = 0 #static variable
	
	def __init__(self,name,year,branch,marks):
		self.name = name
		self.year = year
		self.branch = branch
		self.marks = marks
		Student.studentcount += 1
		self.rollno = Student.studentcount
	
	def printStudentData(self):
		print ""
		print "Name :",self.name
		print "Year :",self.year
		print "Branch :",self.branch
		print "Marks :",self.marks
		print "Roll no",self.rollno
		print ""
	
	@staticmethod    
	def printcount():  
		print "\nSTATIC METHOD CALLED"
		print "Total Count :",Student.studentcount


student1 = Student("ABC","BE","COMP","1082")
student1.printStudentData()
student2 = Student("XYZ","SE","MECH","1000")
student2.printStudentData()
student3 = Student("DEF","TE","ENTC","1000")
student3.printStudentData()

print "Total Students present are:",Student.studentcount

Student.printcount()

