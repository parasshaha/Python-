

def insert(l1):
	if len(l1)!=10:	
		var=input("Enter the data: ")
		l1.append(var)

def delete(l1):
	if len(l1)!=0:
		print("Deleted elementis :",l1.pop())
	else:
		print("Stack is empty")

def display(l1):
	print("Stack elements are:",l1)
	

def isempty(l1):
	if len(l1)==0:
		print("Stack isempty")
	else:
		print("It is not empty")

def isfull(l1):
	if len(l1)==10:
		print("Stack is full")
	else:
		print("Stack is not full")  

def main():
	l1=[]
	while True:
		print("\n1.INsert data\n2.Delete data\n3.Empty\n4.Full\n5.Display\n6.Exit")	
		ch=input("Enter the choice:")
		if ch==1:
			insert(l1)
		elif ch==2:
			delete(l1)
		elif ch==3:
			isempty(l1)
		elif ch==4:
			isfull(l1)
		elif ch==5:
			display(l1)
		elif ch==6:
			break
		else:
			print("Enter valid choice:")
		
	 

if __name__ == '__main__':
	main()	

