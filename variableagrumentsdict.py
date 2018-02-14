


def variableArgsDictDemo(a,b,c,*args,**kwargs):
	print(a,b,c)
	print(type(args))
	for x in args:
		print(x)
	print(type(kwargs))
	for key,value in kwargs.items():
		print(key,value)


def main():
	variableArgsDictDemo(1,2,3,7,8,9,10,name="Paras",profile="Student")


if __name__ == '__main__':
	main()
