n = int(input("Enter the number: "))
b= 90-n+1
for i in range (n):
    for j in range(i+1):
        if j>=i!=0:
            print (chr(b+i-1),end="")
        else :
            print (chr(b+i),end="")
    print ("\n")
