
def patterndiamond():
	no=input("Enter the number of rows")
	for i in range (65,no+1):
		for j in range(no-i):
			print" ",
		for k in range((i*2)-1):
			print chr(k),
		print	

if __name__ == '__main__':
	patterndiamond()

