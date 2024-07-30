#91
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
#95
d=[]
for i in range(20):
        d.append([])
        for j in range(20):
            d[i].append(0)

n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    d[x][y]=1
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()
#96
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
#97
h,w=map(int,input().split())
m=[]
for i in range(h+1):
    m.append([])
    for j in range(w+1):
        m[i].append(0)
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    if d==0:
        for j in range(l):
            m[x][y+j]=1
    else:
        for j in range(l):
            m[x+j][y]=1
for i in range(1,h+1):
    for j in range(1,w+1):
        print(m[i][j], end=' ')
    print()
#98
a=[list(map(int,input().split())) for i in range(10)]
#오= x, y+1 아래=x+1, y
a[1][1]=9
i,j=1,1
while True:
    if a[i][j+1]==0:
            a[i][j+1]=9
            j+=1
    elif a[i][j+1]==1 and a[i+1][j]==0:
            a[i+1][j]=9
            i+=1
    elif a[i][j+1]==2:
            a[i][j+1]=9
            break
    elif a[i+1][j]==2:
            a[i+1][j]=9
            break      
    else:
            break   

for i in range(10):
    for j in range(10):
        print(a[i][j],end=' ')
    print()



