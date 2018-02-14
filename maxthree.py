
def main():

	a=input("ENter the value for a: ")
	b=input("ENter the value for b: ")
	c=input("ENter the value for c: ")

	if a>b and a>c:
		print("A is greater: ",a)
	elif b>c:
		print("B is greater:",b)
	else:
		print("C is greater:",c)


if __name__ == '__main__':
	main()
	
