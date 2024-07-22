#77
n = int(input())
s = 0
for i in range(1, n+1):
  if i%2==0:
    s +=i

print(s)
#78
while(True):
    c = input()
    if c == "q":
        print(c)
        break
    print(c)
#79
n= int(input())
hap=0
for i in range(1,1001):
       hap+=i
       if hap>=n:
            print(i)
            break
#80
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
     
        print(i, j)
#81
n=int(input(),16)
for i in range(1,16):
   print("%x".upper()%n,"*","%x".upper()%i, "=", "%x".upper()%(n*i), sep="")
#82
n = int(input())
for i in range(1, n + 1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("X", end=' ')
    else:
#83

r, g, b = map(int, input().split())


count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1

print(count)
#84
h, b, c, s = map(int, input().split())

print(format(h * b * c * s / 8 / 1024 / 1024, ".1f"), "MB")

#85
w, h, b = map(int, input().split())

print(format(w * h * b / 8 / 1024 / 1024, ".2f"), "MB")
#86
n= int(input())
sum=0
for i in range(1,n+1):
    if sum>=n:
        break
    sum+=i
print(sum)
#87
n= int(input())
for k in range(1,n+1):
    if k%3==0:
        continue
    print(k,end=" ")
#88
a,d,n=map(int,input().split())
print(a+d*(n-1))
#89
a, r, n = map(int, input().split())
print(a * r**(n-1))
#90
a, m, d, n = map(int, input().split())
for i in range(1, n):
    a = a * m + d
print(a)
#91
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)




















        


        
        print(i, end=' ')


