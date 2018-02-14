
def drawpattern(a,b):
	for i in range(a,b+1):
		x=a		
		for j in range(i):
			print chr(x+j),
	
def main():
	a=ord(input("enter the starting character"))
	b=ord(input("enter the ending character"))
	drawpattern(a,b)	
		

	

if __name__ == '__main__':
	main()



