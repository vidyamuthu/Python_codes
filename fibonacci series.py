#8.Fibonacci series
n=int(input("Enter the number limit:"))
n1=0
n2=1
count=0
if(n<=0):
    print("Enter the positive number")
elif(n==1):
    print("The prime number sequence of",n,":")
    print(n1 , n2)
else:
    while(count < n):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        
