
def accept():
	crc=input("Enter the value for CRC: ")
	length1=input("Enter the value of length: ")
	data=input("Enter the value for data: ")
	flag=input("Enter the value for flag: ")
	result1=packeting(crc,length1,data,flag)
	return result1

def packeting(crc,length1,data,flag):
	x=2**5-1
	y=2**8-1
	z=2**18-1
	n=2**1-1
	crc_ex=crc&x
	length1_ex=length1&y
	data_ex=data&z
	flag_ex=flag&n
	packet=0
	packet=crc_ex
	packet<<8
	packet=packet | length1_ex
	packet<<18
	packet=packet | data_ex
	packet<<1
	packet=packet| flag_ex
	return packet

def main():
	output=accept()
	print("vaule of packet is : ",output)

if __name__ == '__main__':
	main()
	
