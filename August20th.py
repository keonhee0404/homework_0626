N = input().strip()
n = list(N)
for i in range(len(n) - 1):
    max_idx = i
    for j in range(i + 1, len(n)):
        if n[j] > n[max_idx]:
            max_idx = j
            n[i], n[max_idx] = n[max_idx], n[i]



print(n)



#11391
N = int(input().strip())
for _ in range(N):
  a=list(map(int,input().split()))
for i in range(N-1):
    max_idx = i
    for j in range(i + 1, N):
        if a[j] > a[max_idx]:
            max_idx = j
    a[i], a[max_idx] = a[max_idx], a[i]
for num in a:
    print(a)
#11339
N = int(input())
a = list(map(int, input().split()))
n = len(a)
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
time=[]
current_sum=0
for i in a:
    current_sum+=i
    time.append(current_sum)

print(sum(time))

