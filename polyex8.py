#polyex8.py
class India:
	def capital(self):   # original method
		print("Delhi is the capital of India")
	
	def lang(self):    # original method
		print("Hindi / Mixed Lang Indian can speack")

	def  type(self):   # original method
		print("India is a developping.... Country")
class USA:
	def capital(self):  
		print("WashingTon is the capital of USA")
	def lang(self):   
		print("English Lang, Americans can speack")
	def  type(self):  
		print("USA is a developped Country")
#main program
uo=USA()
ind=India()
print("----------------------------------------------------")
for obj in [uo,ind]:   # here we are using object level polymorphism
	print("Ref of obj=",type(obj))
	obj.capital()
	obj.lang()
	obj.type()
	print("-----------------------------------------")
