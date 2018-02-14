def fromkeysss(input_dict,output_dict_values):
	result_dict={}
	keys_list=[]
	if type(output_dict_values)==list or type(output_dict_values)==tuple:
		keys_list=input_dict.keys()
		values_length=len(output_dict_values)
		for i in range(len(keys_list)):
			if i < values_length:
				result_dict[keys_list[i]]=output_dict_values[i]
			else:
				result_dict[keys_list[i]]=None
	else:
		result_dict=dict.fromkeys(input_dict,output_dict_values)
	return result_dict


def main():
	d={1:2,2:3,4:5}
	z=input("Enter the value for updating or creating new dictionary")
	outt=fromkeysss(d,z)
	print d
	print outt

if __name__ == '__main__':
	main()
