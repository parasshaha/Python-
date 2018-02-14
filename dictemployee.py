emp_id=0
emp={}
def accept():
	dict_in={}
	name,DOB,address,salary=input("Enter the name,DOB,address,salary")	
	dict_in["name"]=name
	dict_in["DOB"]=DOB
	dict_in["address"]=address
	dict_in["salary"]=salary
	return dict_in

def insert():
	global emp_id
	emp_id+=1	
	emp_data=accept()
	print emp_data
	emp[emp_id]=emp
	print emp

def main():
	insert()

if __name__ == '__main__':
	main()
