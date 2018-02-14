
def isodd(no1,no2):
	for x in range(no1,no2):
		if (x&1) ==1:
			print(x)


def main():
	no1,no2=input("Enter the lower and upper bound for range :")
	if no1<no2:
		isodd(no1,no2)
	else:
		print("lower bound is greater then upper bound ")
		
if __name__ == '__main__':
	main()
