

def checkmultiple(no):
	if no&(2**5-1) ==0:
		print("It is multiple of 32")
	else:
		print("It is not multiple of 32")

def main():
	no=input("Enter the no ")
	checkmultiple(no)



if __name__ == '__main__':
	main()
