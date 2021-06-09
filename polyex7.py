#polyex7.py
class India:
	def capital(self):   # original method
		print("Delhi is the capital of India")
	
	def lang(self):    # original method
		print("Hindi / Mixed Lang Indian can speack")

	def  type(self):   # original method
		print("India is a developping.... Country")
class USA(India):
	def capital(self):   # overridden method
		print("WashingTon is the capital of USA")
		India.capital(self)
		print("----------------------------------------------------------")
	def lang(self):    # overridden method
		print("English Lang, Americans can speack")
		super().lang()
		print("----------------------------------------------------------")
	def  type(self):  # overridden method
		print("USA is a developped Country")
		super().type()
		print("----------------------------------------------------------")
#main program
uo=USA()
uo.capital()
uo.lang()
uo.type()
