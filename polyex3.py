#polyex3.py
class Circle(object):
	def   draw(self):#original method
		print("Drawing Circle--Circle class:")

class Rect:
	def  draw(self): 
		print("Drawing Rect--Rect class:")

class Triangle:
	def  draw(self): 
		print("Drawing Triangle--Triangle class:")
		
class Square(Triangle, Rect, Circle ):
	def  draw(self): # overridden method
		print("Drawing Square--Squar class:")
		Circle.draw(self)
		Triangle.draw(self)
		Rect.draw(self)

#main program
so=Square()
so.draw();
