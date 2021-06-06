#polyex5.py
class Circle:
	def  area(self,r):# original method
		ac=3.14*r*r
		print("Area of Circle=",ac)

class Rect (Circle):
	def area(self,l,b):# overridden method
		ar=l*b
		print("Area of Rect=",ar)
		
class Square(Rect):
	def area(self,s):  # overridden method
		as1=s*s
		print("Area of Square=",as1)
		print("----------------------------------------")
		super().area(float(input("Enter Length of Rect:")),float(input("Enter breadth of Rect:")))
		print("----------------------------------------")
		Circle.area(self,float(input("Enter Radious of Circle:")))

# main program
so=Square()
so.area(float(input("Enter Side of Square:")))
