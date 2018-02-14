

def factorial(no):	
	if no==0:
		return 1	
	return no*factorial(no-1)

def main():
	no=input("Enter the number : ")
	result=factorial(no)
	print("Facotrial of number{} is {}".format(no,result))

if __name__== '__main__':
	main()
