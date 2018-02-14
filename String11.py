def checkingstr(str1):
	if len(str1)<3:
		return str1
	elif str1[-3:] =="ing":
		return str1[:-3]+"ly"
	else:
		return str1+"ing" 

def main():
	str1=input("Enter the string : ")
	outstr1=checkingstr(str1)
	print("Verb of {} is {}".format(str1,outstr1))

if __name__ == '__main__':
	main()
