def additionvariablearguments(*args):
	sum=0	
	for x in args:
		sum=sum+x
		
	return sum


def main():

	list1=additionvariablearguments(15,2,65,58,2,22,53)
	print("Addition of first list is :",list1)


if __name__=='__main__':
	main() 
