import time
a=time.time()
def fibonacci(n):
     
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(40))
print(time.time()-a)