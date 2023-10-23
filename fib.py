class myFibonacci:
    def __init__(self, fibRange):
        self.Range = fibRange
        self.Fibonacci = []
        self.setFibonacci()
          
    def setFibonacci(self):
        self.Fibonacci = []
        self.Fibonacci.append(0)
        self.Fibonacci.append(1)
        for n in range(2, self.Range + 1):
            self.Fibonacci.append(self.Fibonacci[n-1] + self.Fibonacci[n-2])
            
    def getFibonacci(self):
        return(self.Fibonacci)

def main():
    f = myFibonacci(20)

    print('{:>10} {:>10}'.format('n', 'Fib'))
    i= 0
    for n in f.getFibonacci():
        i += 1
        print('{:>10} {:>10}'.format(i-1, n))

if __name__== '__main__':
    main()



