class check_list():
	def __init__(self):
		self.n = []
	def add_list(self , a):
		return self.n.append(a)
	def delete_list(self,d):
		self.n.remove(d)
	def display_list(self):
		return self.n
	

list1 = check_list()
choice = 1
print("1: Add")
print("2: Remove")
print("3: Display")
print("4: Exit")


while choice != 0:
	if choice ==1:
		n = int(input("Enter choice for list opearation:"))
		list1.add_list(n)
		print("List : ", list1.display_list())
	elif choice ==2 :
		n = int(input("Enter choice for list opearation:"))
		list1.delete_list(n)
		print("List : ", list1.display_list())
	elif choice ==3:
		print("List : ", list1.display_list())
	else:
		print("Exit the list")
		break
