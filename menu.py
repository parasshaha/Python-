def menu():
    print "Select ant Operaion: "
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit"
    print " "
    return input ("Choose your option: ")
 
def add(a,b):
    print (a + b)
 
def sub(a,b):
    print (b - a)
 
def mul(a,b):
    print (a * b)
 
def div(a,b):
    print (a / b)
 

lp = 1
choice = 0
while lp == 1:
    choice = menu()
    if choice == 1:
        add(input("First number: "),input("Second number: "))
    elif choice == 2:
        sub(input("First number: "),input("Second number: "))
    elif choice == 3:
        mul(input("First number: "),input("Second number: "))
    elif choice == 4:
        div(input("First number: "),input("Second number: "))
    elif choice == 5:
        lp = 0
 
print "Thankyou!"
