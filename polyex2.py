#polyex2.py
class Circle(object):
	def   __init__(self):#original constructor
		print("Drawing Circle--Circle class:")

class Rect(Circle):
	def  __init__(self): # overridden constructor
		super().__init__() #calling    __int__() of Circle class
		print("Drawing Rect--__init__(self):")
		
class Square(Rect):
	def  __init__(self):  # overridden constructor
		super().__init__() #calling    __int__() of Rect class
		print("Drawing Square-- __init__(self):")

		
#main program
so=Square()
