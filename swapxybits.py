
def swapbits(number1,number2,position,bits):
	x=2**bits-1
	x=x<<(position-bits)
	x_part=number1&x
	y_part=number2&x
	number1=number1&~x
	number2=number2&~x
	number1=number1|y_part
	number2=number2|x_part
	print("After swapping the number1 And number2 is :",number1,number2)	
def main():
	number1=input("Enter the number 1: ")
	number2=input("Enter the number 2: 	")
	position=input("Enter the position of bit")
	bits=input("enter how many bits you want to toggle:")
	print("Before swapping the number1 And number2 is :",number1,number2)	
	swapbits(number1,number2,position,bits)

if __name__ == '__main__':
	main()
