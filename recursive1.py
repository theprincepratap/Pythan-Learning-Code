#Write a recursive function in python to add first n natural numbers 
n=int(input("Enter Number : "))

def nsum(n):
    if n == 1 :
        return 1
    s=n+nsum(n-1)
    return s
sum=nsum(n)
print (sum)