
def turnoffrightmostonebit(no):
	ch=1
	if no!=0:	
		while(no&ch)==0:
	  		ch=ch<<1
	return no&~ch

def main():
	no=input("Enter the no ")
	result=turnoffrightmostonebit(no)
	print("Number is : ",result)


if __name__ == '__main__':
	main()
