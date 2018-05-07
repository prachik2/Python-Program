print('Calculator')
amount = float(input("Enter amount"))
roi = float(input("Enter roi"))
time = float(input("Enter time"))

total = (amount * pow(1 + (roi/100), time))
interest = total - amount
print("\n interest = %0.2f" %interest)
