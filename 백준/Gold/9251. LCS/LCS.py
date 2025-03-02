# LCS

A = list(input())
B = list(input())

table = [[0] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i - 1] == B[j - 1]:  # 문자가 같으면
            table[i][j] = table[i - 1][j - 1] + 1
        else:  # 문자가 다르면 이전 값 중 최대값 사용
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

# LCS 길이 출력
print(table[len(A)][len(B)])