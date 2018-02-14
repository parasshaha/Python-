

def variablenumberofagruments(*args):
	print(type(args))
	for x in args:
		print(x)	
def main():
	variablenumberofagruments(1,2,3,4)
	variablenumberofagruments(20,30,104,"hi","bye")


if __name__ == '__main__':
	main()
