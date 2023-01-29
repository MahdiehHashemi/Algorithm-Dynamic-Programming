# 30, 10, 60, 10, 60, 50  greedy failure / DP or recursion 
##only one or two steps in one time
s = [30, 10, 60, 10, 60, 50]                  # energy at each station
c=[0,20]
for i in range (2,len(s)):
    c1=c[i-1]+abs(s[i]-s[i-1])
    c2=c[i-2]+abs(s[i]-s[i-2])
    c.append(min(c1,c2))
print(c)