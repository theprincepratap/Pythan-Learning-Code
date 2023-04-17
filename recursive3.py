#write a recursive program to print factorial of a number 
n = int(input("Enter Number :"))
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

factorial = fact(n)
print (factorial)