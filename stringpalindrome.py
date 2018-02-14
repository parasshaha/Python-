

def Ispalindrome(usrname):
	return usrname==usrname[::-1]
def main():
	usrname=input("Enter the String :")
	#temp=usrname[::-1]	
	if Ispalindrome(usrname):
		print("String %s is palindrome"%(usrname))
	else:
		print("String %s is not palindrome"%(usrname)) 


if __name__ == '__main__':
	main()
