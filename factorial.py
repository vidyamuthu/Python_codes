#6.factorial of a number
a=int(input("Enter the number:"))
f=1
for i in range(1,a+1):
    f*=i
print("The factorial of",a,":",f)    
