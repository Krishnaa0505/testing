def fact(a):
    n=1
    for i in range(1,a+1):
        n*=i
    
    print(f"The factorial of {a} is {n}")
    #return n

if __name__ == '__main__':
    n=int(input("Enter the number to find factorial of"))#input here is being modified again
    fact(n)
