print ("\t\t\tlucky number finder")
import random
def login():
	x=input("user name:-\t")
	y=input ("password:-\t")
	if x=="billa" and y=="12345":
		print("sucessfully loged in !!!")
		import random
		def main():
			a= input("What is your name?\t")
			b= random.randint(1, 100)
			print(f"Hello, {a}! Your lucky number is {b}.")
		if __name__=="__main__":
				main()
				
	elif x=="billa" and y!="12345":
		print("wrong password ???")
		login()
	elif x!="billa" and y=="12345":
		print("invalid user !!!")
		login()
	else:
		print ("enter valid details !!!")
		login()
print ("welcome")
login()
	
		