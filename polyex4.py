#polyex4.py
class Circle(object):
	def   __init__(self):#original constructor
		print("Drawing Circle--Circle class:")

class Rect:
	def  __init__(self):
		print("Drawing Rect--__init__(self):")
class Triangle:
	def  __init__(self): 
		print("Drawing Triangle--__init__(self):")
		
class Square(Rect,Circle,Triangle):
	def  __init__(self):  # overridden constructor
		print("Drawing Square-- __init__(self):")
		Circle.__init__(self)
		Rect.__init__(self)
		Triangle.__init__(self)
		
#main program
so=Square()
