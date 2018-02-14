def addition():
	lower=int(input("Enter the lower limit for the range:"))
	upper=int(input("Enter the upper limit for the range:"))
	total = 0
	for i in range(lower,upper+1):
    	if(i%2!=0):
			total+=i
        	print(i)
	print ("addition of all odd numbers is-")
	print (total)

def main():
	addition()


if __name__ == '__main__':
	main()
