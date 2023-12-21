print ("\t\t\tAge Calculator")
def login():
	a=input("user name:-\t")
	b=int(input("enter password:-\t"))
	if a=="abc" and b== 123:
		print ("")
		print ("sucessfully loged in !!!!")
		print("")
		x=int(input ("Please enter your birth year:-\t"))
		y=2023
		print ("your age is:-",y-x)
		print ("\t\tThank you !!!")
	elif a!=abc and b==123:
		print ("invalid user !!!")
		print ("try again ???")
		login()
	elif a==abc and b!=123:
		print ("wrong password !!!")
		print ("try again ???")
		login()
	else:
		print("try again ???")
		login()
z=input("press any key to log in process")
print ( "\t\twelcome to age calculator !!!")
login()
	
		
