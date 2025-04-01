# 틱택토
cases = [[0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

while True:
    tictacto = list(input())

    if tictacto[0] == 'e': # "end" 입력으로 종료
        break

    cnt_x = tictacto.count('X') # "X"의 개수
    cnt_o = tictacto.count('O') # "O"의 개수

    if cnt_o > cnt_x or (cnt_x - cnt_o) > 1: # X가 O보다 1개 많거나 같아야 함
        print("invalid")

    else:
        x_win = 0
        o_win = 0

        for i, j, k in cases:
            if tictacto[i] == tictacto[j] == tictacto[k] and tictacto[i] != ".":
                if tictacto[i] == "X":
                    x_win += 1
                else:
                    o_win += 1

        # 결과 출력
        if x_win > 0 and o_win > 0: # 둘 다 이길 순 없음
            print("invalid")
        elif x_win == 0 and o_win == 0: # 비김
            if cnt_x + cnt_o == 9:
                print("valid")
            else:
                print("invalid")

        elif x_win >= 1 and o_win == 0 and (cnt_x-cnt_o) == 1:
            print("valid")

        elif o_win >= 1 and x_win == 0 and cnt_o == cnt_x:
            print("valid")

        else:
            print("invalid")
