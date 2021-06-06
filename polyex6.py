#polyex6.py
class Circle:
	def  area(self,r):# original method
		print("----------------------------------------")
		ac=3.14*r*r
		print("Area of Circle=",ac)

class Square:
	def area(self,s):  # overridden method
		print("----------------------------------------")
		as1=s*s
		print("Area of Square=",as1)

class Rect :
	def area(self,l,b=12):# overridden method
		print("----------------------------------------")
		ar=l*b
		print("Area of Rect=",ar)
		
#main program
co=Circle()
so=Square()
ro=Rect()
lst=[]
lst.append(co)
lst.append(so)
lst.append(ro)
for obj in lst:
	obj.area(3)
print("-------------------------------------------")
for obj in (co,ro,so):
	obj.area(6)
