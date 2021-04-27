H,V=input().split()
x=[3,4,1,2]

for i in range(int(H)):
    x[1],x[0]=x[0],x[1]
    x[2],x[3]=x[3],x[2]

for i in range(int(V)):
    x[1],x[0]=x[0],x[1]
    x[2],x[3]=x[3],x[2]

a=x[0]
b=x[1]
c=x[2]
d=x[3]
print(a,b)
print(c,d)












