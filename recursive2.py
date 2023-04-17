n = int(input("Enter number : "))
def nsqure(n):
    if n==1 :
        return 1
    return n*n + nsqure(n-1)
sumsquare=nsqure(n)
print (sumsquare)