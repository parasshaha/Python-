def countingchar(input_str):
	i=0
	count=0
	result_dict={}	
	while i <len(input_str):
		if result_dict.has_key(input_str[i]):
			result_dict[input_str[i]]=result_dict[input_str[i]]+1
		else:
			result_dict[input_str[i]]=1
		i+=1	
	return result_dict


def main():
	input_str=input("Enter the string: ")
	out_str=countingchar(input_str)
	print out_str




if __name__ == '__main__':
	main()
	
