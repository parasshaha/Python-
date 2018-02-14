

def mappingkeys(d,z):
	x=0
	zz={}
	if type(z)==int or type(z)==str:
		print(type(z))
		zz=dict.fromkeys(d,z)
	elif type(z)==tuple:
		z=list(z)
		print(type(z))
		for key in d:
			if x!=len(z):
			 zz[key]=z[x]
			 x+=1
	print zz
	print d

def main():
	d={1:2,2:3,4:5}
	z=input("Enter the value for updating or creating new dictionary")
	mappingkeys(d,z)


if __name__ == '__main__':
	main()
	
