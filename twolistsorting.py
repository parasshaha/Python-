def sorting(l11):
	for x in range(len(l11)):
		for y in range(x+1,len(l11)):
			if l11[x]>l11[y]:
				temp=l11[x]
				l11[x]=l11[y]
				l11[y]=temp
	return l11
	

def merge(l1,l2,l3):
	
	i=j=0	
	while i < len(l1) and j<len(l2):
		if l1[i]<l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i<len(l1):
		l3.extend(l1[i:])
	if j<len(l2):
		l3.extend(l2[j:])
	return l3	
def main():
	l1=[]
	l2=[]
	l3=[]
	l1=list(input("Enter the elements for list1: "))
	l2=list(input("Enter the elements for list2: "))
	sorting(l1)
	sorting(l2)
	print("First list after $orting",l1)
	print("Second li$t after sorting",l2)
	l3=merge(l1,l2,l3)
	print("FINAL LIST",l3)

if __name__ == '__main__':
	main()
	
