
def checkpower(no):
	return (no&(no-1)==0
def main():
	no=input("Enter the no ")
	result=checkpower(no)
	print("number is 2's power",result)


if __name__ == '__main__':
	main()
