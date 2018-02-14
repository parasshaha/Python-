
def accept():
	crc=input("Enter the value for CRC: ")
	length1=input("Enter the value of length: ")
	data=input("Enter the value for data: ")
	flag=input("Enter the value for flag: ")
	result1=packeting(crc,length1,data,flag)
	return result1

def packeting(crc,length1,data,flag):
	packet=crc
	packet=packet<<8
	packet=packet | length1 &((1<<8)-1)
	packet=packet<<18
	packet=packet| data &((1<<18)-1)
	packet=packet<<1
	packet=packet | flag &((1<<1)-1)
	return packet

def depacketing(packet):
	flag=packet&((1<<1)-1)
	packet=packet>>1
	data=packet&((1<<18)-1)
	packet=packet>>18
	length=packet&((1<<8)-1)
	packet=packet>>8
	crc=packet&((1<<5)-1)
	return crc,length,data,flag	
	
def main():
	output=accept()
	print("vaule of packet is : ",output)
	no1,no2,no3,no4=depacketing(output)
	print("after depacketing:",no1,no2,no3,no4)
if __name__ == '__main__':
	main()
	
