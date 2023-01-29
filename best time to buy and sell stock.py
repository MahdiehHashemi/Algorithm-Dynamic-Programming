# this code is nor=t working as the index of repeated elements can not be recognized in the list!!!!
prices = [2,1,2,0,1]#[7,1,5,3,6,4]  ##[7,6,4,3,1]
#a=[7,6,4,3,1]
a=sorted(prices)
c=0
print(prices.index(2))
for i in range (len(prices)):
    if c==0:
        for j in range(len(prices)-1,i,-1):
            if a[j]-a[i]>0 and prices.index(a[i])<prices.index(a[j]):
                print(a[j]-a[i])
                c=1
                break

if c==0:
    print(0)
         

    