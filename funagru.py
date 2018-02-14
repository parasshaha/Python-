

def adder(a,b,c=0,d=0,e=0):
	return a+b+c+d+e


def main():	
	print adder(10,20) 
	print adder(10,20,30)
	print adder(10,20,33,44)
	print adder(10,20,1,2,3)

if __name__ == '__main__':
	main()

