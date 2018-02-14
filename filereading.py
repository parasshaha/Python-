def main():
	fd=open("abc.txt")
	line=fd.readline()	
	while line!="":
		print(line)
		line=fd.readline()
	
if __name__ == '__main__':
	main()

