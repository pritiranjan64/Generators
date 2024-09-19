# series of number
def Series(sv,ev,up=1):
    i=sv
    while i<ev:
        yield i
        i+=up
s=Series(1,10,2)
for k in s:
    print(k)   


# Fibonacci number
def FibonacciNumber(fv,sv,n):
    i=1
    while i<=n:
        yield fv
        fv,sv=sv,fv+sv
        i+=1
f=FibonacciNumber(2,3,7)
for k in f:
    print(k)
