def countingchar(input_str):
	i=0
	result_str=""	
	while i <len(input_str):
		char_check=input_str[i]
		count=1
		while i+1 < len(input_str) and input_str[i+1]==char_check:
			count+=1
			i+=1
		result_str+=char_check+str(count)
		i+=1
	return result_str


def main():
	input_str=input("Enter the string: ")
	out_str=countingchar(input_str)
	print out_str




if __name__ == '__main__':
	main()
	
