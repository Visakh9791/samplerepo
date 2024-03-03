def fibonacci(n):
    #Base class are 0 & 1 in fibonacci series
    #if n == 0:
    #    return 0
    #if n == 1:
    #    return 1
    # use it short
    if n <= 1:
        return n
        
    #5th term = 4th term + 3rd term
    #4th term = 3term + 2term
    #use recursive function calling and return it ...(n-1)+(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

num=int(input())
result=fibonacci(num)
print(result)