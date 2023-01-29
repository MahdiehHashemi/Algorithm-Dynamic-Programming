def number_of_ones(n):
    a=[0]
    offset=1
    for i in range (1,n+1):
        if offset*2==i:
            offset=i
        a.append(1+a[i-offset])
    return a  
    
print(number_of_ones(10))