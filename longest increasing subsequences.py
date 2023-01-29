a=[1,2,4,3]
LIS=[1]*len(a)
# print(LIS)
for i in range (len(a)-1,-1,-1):
    LISj=[]
    for j in range (i+1,len(a)):
        if a[i]<a[j]:
            LIS[i]=max(LIS[i],1+LIS[j])
print(max(LIS))
