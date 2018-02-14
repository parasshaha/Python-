
def countones(no):
	ch=1
	count=0	
	while ch<=no: 
		if (no&ch)!=0:
	  		count+=1
		ch=ch<<1 
	return count

def main():
	no=input("Enter the no ")
	result=countones(no)
	print("Number of one's if ",result)


if __name__ == '__main__':
	main()
