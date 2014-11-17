#finds the nth fibbonaci number 
#Write a function fib() that a takes an integer n and returns the nth fibonacci number.

class NthFibbonacci:
    
    def nthFib(self, fib):
        if(fib<1):
            return "index can't be a negative number"
        elif(fib==1):
            return 1
        else:
            previous=0
            current=1
           
            for i in range(1,fib):
                fib=current+previous
                previous=current
                current=fib
    
            return fib
    
    
x=NthFibbonacci()
print x.nthFib(10)