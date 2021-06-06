#polyex1.py
class Circle(object):
	def   draw(self):#original method
		print("Drawing Circle--Circle class:")

class Rect(Circle):
	def  draw(self): # overridden method
		super().draw() # will call draw() of Circle class
		print("Drawing Rect--Rect class:")
		
class Square(Rect):
	def  draw(self): # overridden method
		super().draw() # will call draw() of Rect class
		print("Drawing Square--Squar class:")
		

#main program
so=Square()
so.draw();
