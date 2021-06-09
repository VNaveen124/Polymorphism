#polyex10.py
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

class Country:
	@staticmethod
	def dispCountryInfo(obj):
		print("----------------------------------------------------")
		obj.capital()
		obj.lang()
		obj.type()
		print("----------------------------------------------------")

#main program
uo=USA()
ind=India()
for kvobj in (ind,uo):
	Country.dispCountryInfo(kvobj)
