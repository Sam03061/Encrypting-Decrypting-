import random 
import string 

L=input("Paste your writtings : ")
c=L.split()
j=len(c)
uni=""

sump=""
for i in range(j):
    c0=random.choice(string.ascii_lowercase)
    z0=random.choice(string.ascii_lowercase)
    d0=random.choice(string.ascii_lowercase)
    c1=random.choice(string.ascii_lowercase)
    d1=random.choice(string.ascii_lowercase)
    z1=random.choice(string.ascii_lowercase)
    x=c[i]
    if(len(x)<3 and len(x)>1):
        if(i==0):
            jango=x[1]+x[0]
            sump=c1+d1+z1+jango+c0+z0+d0
            uni=uni+sump
            

        else:
         jango=x[1]+x[0]
         sump=c1+d1+z1+jango+c0+z0+d0
         uni=uni+" "+sump
    else:
        f=x[:1]
        l=x[1:]
        l=l+f #have to turn this 
        leng=len(l)
        toti=""
        for n in range(leng-1,-1,-1):
            toti=toti+l[n]
        sump=c1+d1+z1+toti+c0+z0+d0
        uni=uni+" "+sump
print(uni)