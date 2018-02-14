
def gcdno(no1,no2):
	if no1==no2:
		return no1
	else:
		if no1>no2:
			no1=no1-no2
		else:
			no2=no2-no1
		return gcdno(no1,no2)
	
def main():
	no1,no2=input("Enter any two number : ")
	res=gcdno(no1,no2)
	print("GCD of given number is",res)		

if __name__ == '__main__':
	main()
