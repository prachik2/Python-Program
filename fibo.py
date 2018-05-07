a = int(input("1st number"))
b = int(input("2nd number"))
n = int(input("length of series"))
fibo_list = []
fibo_list.append(a)
fibo_list.append(b)
print("Fibbo Series", fibo_list)
while (n-2):
	temp = a + b
	a = b
	b = temp
	fibo_list.append(temp)
	n = n-1

print(fibo_list)
