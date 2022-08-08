#5.Prime number in the interval
a=int(input("Enter the starting interval:"))
b=int(input("Enter the ending interval:"))
print("The prime number between a and  b:")
for num in range(a,b+1):
    if(num>1):
        for i in range(2,num):
            if(num%2==0):
                break
        else:
            print(num)
