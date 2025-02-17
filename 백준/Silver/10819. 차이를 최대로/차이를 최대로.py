#차이를 최대로
N = int(input())
arr = list(map(int, input().split()))
goal = 0

def f(arr, visited, per):
    if len(per) == len(arr):
        calculator(per)
        return

    for n in range(len(arr)):
        if not visited[n]:
            visited[n] = 1
            f(arr, visited, per + [arr[n]])
            visited[n] = 0


def calculator(P):
    global goal
    result = 0
    for i in range(len(P)-1):
        result += abs(P[i]-P[i+1])
    if result >= goal:
        goal = result

visited = [0]*(N+1)

f(arr, visited, [])
print(goal)
