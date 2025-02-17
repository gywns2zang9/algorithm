#윳놀이
for n in range(3):
    game = list(map(int, input().split()))
    cnt = 0
    for i in range(4):
        if game[i] == 0:
            cnt += 1

    case = ["E", "A", "B", "C", "D"]
    print(case[cnt])