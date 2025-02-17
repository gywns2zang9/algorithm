A = int(input())
B = int(input())
C = int(input())

ABC = A*B*C
num = [0]*10
k = len(str(ABC))

for i in range(k-1, -1, -1):
    x = ABC // (10**i)
    num[x] += 1
    ABC = ABC % (10**i)

for j in range(10):
    print(num[j])
