

def checkmultiple(no1,no2):
	for x in range(no1,no2+1):
		if x%2==0 or x%3==0:
			continue
		else:
			print(x)


def main():
	no1,no2=input("Enter the lower and higher bound : ")
	checkmultiple(no1,no2)

if __name__ == '__main__':
	main()
	
