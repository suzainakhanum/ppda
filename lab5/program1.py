def calculator(num1,num2):
	num1=int(input("enter the number"))
	num2=int(input("enter the number"))
	choice=input("enter the choice")
	if (choice == "%"):
		print(num1%num2)
	elif (choice == "/"):
		print(num1/num2)
	elif (choice == "**"):
		print(num1**num2)
	else:
		return num1+num2
		
kal=calculator(10,20)
print(kal)	
