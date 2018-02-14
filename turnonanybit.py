
def turnoff(number,position,bits):
	x=2**bits-1
	x=x<<(position-bits)
	return number|x	 

def main():
	number=input("Enter the number : ")
	position=input("Enter the position of bit")
	bits=input("enter how many bits you want to turn on:")
	if bits<=position:	
		result=turnoff(number,position,bits)
		print("The number is: ",result)	
	else:
		print("Enter the valid input") 

if __name__ == '__main__':
	main()
	
