import time
a=time.time()
def fibb(n):
    if n==1 or n==2:
        f=1
    else:
        f=fibb(n-1)+fibb(n-2)
    return(f)
print(fibb(40))
print(time.time()-a)