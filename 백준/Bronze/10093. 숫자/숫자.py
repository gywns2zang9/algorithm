#숫자
A, B = map(int, input().split())
if A == B:
    print(0)
if A > B:
    A, B = B, A
if B > A:
    print(B-1-A)
for i in range(A+1, B):
    print(i, end=" ")