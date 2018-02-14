def factorial(no):	
	fact=-1	
	if no > 0:
		if no < 3:
			fact=no
		else:
			fact=1
			while no!=1:
				fact=fact*no
				no-=1
				
	return fact

def main():
	no=input("Enter the number : ")
	result=factorial(no)
	print("Factorial of number {} is {}".format(no,result))

if __name__== '__main__':
	main()
