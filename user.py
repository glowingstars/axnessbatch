class Select:
	username1="ravalireddy"
	password1="reddy123"
	def choice(self):
		print("enter\n1 for new registre\n2 for already registered")
		choice=input("enter your choice")
		if(choice=="1"):
			print("welcome")
			
			username=input("enter your first name")
			
			password=input("enter your passsword includes nmbers and alphabets")
		
			if(password.isalnum):
				print("you have sucessfully registered")
			else:
				print("please enter the password  which includes numbers and alphabets")
		elif(choice=="2"):
			username2=input("enter your username")
			if(username1==username2):
				password2=input("enter your password")
				if(password1==password2):
					print("you have sucessfully login to  this page")
				else:
					print("you have entered incorrect password")
			else:
				print("you have entered incorrect username")
		else:
			print("please select correct  choice")


if __name__=='__main__':
	p=Select()
	p.choice()


			