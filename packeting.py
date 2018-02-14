
def accept():
	crc=input("Enter the value for CRC: ")
	length1=input("Enter the value of length: ")
	data=input("Enter the value for data: ")
	flag=input("Enter the value for flag: ")
	protocol=input("Enter the value for protocol: ")
	result1=packeting(crc,length1,data,flag,protocol)
	return result1

def packeting(crc,length1,data,flag,protocol):
	packet=crc
	packet=packet<<7
	packet=packet | length1 &((1<<7)-1)
	packet=packet<<16
	packet=packet| data &((1<<16)-1)
	packet=packet<<2
	packet=packet | flag &((1<<2)-1)
	packet=packet<<4
	packet=packet | protocol &((1<<4)-1)
	return packet

def depacketing(packet):
	protocol=packet&((1<<4)-1)
	packet>>4	
	flag=packet&((1<<2)-1)
	packet=packet>>2
	data=packet&((1<<16)-1)
	packet=packet>>16
	length=packet&((1<<7)-1)
	packet=packet>>7
	crc=packet&((1<<3)-1)
	return crc,length,data,flag,protocol	
	
def main():
	output=accept()
	print("vaule of packet is : ",output)
	no1,no2,no3,no4,no5=depacketing(output)
	print("after depacketing:",no1,no2,no3,no4,no5)
if __name__ == '__main__':
	main()
	
