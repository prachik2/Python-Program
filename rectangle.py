class rectangle_area():
	def __init__(self, height,width):
		self.height = height
		self.width = width
	
	def area(self):
		return (self.height * self.width)

a = float(input("Enter Height of area"))
b = float(input("Enter Weight of area"))

re_object = rectangle_area(a,b)
print("Area: " ,re_object.area())
print()
