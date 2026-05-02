x=input()
c=x.split()
genth=len(c)
uni=""
for i in range(genth):
    sum=""
    y=c[i]
    y=y[3:-3]
    fenth=len(y)
    for u in range(fenth-1,-1,-1):
        sum=sum+y[u]
    if(fenth>2):
        rem=sum[-1:]
        sum=sum[:-1]
        sum=rem+sum
    uni=uni+" "+sum 
print(uni)


    
