N ,M = map(int, input().split())
A = set(map(int, input().split()))
B = list(map(int, input().split()))
cnt = N
for b in B:
    if b in A:
        cnt -= 1
    else:
        cnt +=1

print(cnt)