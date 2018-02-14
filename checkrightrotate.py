
def checkrot(str1,str2):
	if len(str1)==len(str2):
		str3=str1+str1
		ad=str3.__contains__(str2)
		if ad==True:
			print("it is right rotate")
		else:
			print("It is not right rotate ")
	else:
		print("It is invalid string.Out of range") 

def main():
	str1=input(" Enter the first String : ")
	str2=input("Enter the second String: ")
	checkrot(str1,str2)	

if __name__ =='__main__':
	main()
