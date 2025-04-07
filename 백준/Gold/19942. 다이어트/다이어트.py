# 다이어트
N = int(input()) # 식재료
min_nutrient = list(map(int, input().split()))
foods = [list(map(int, input().split())) for _ in range(N)] # [단백질, 지방, 탄수화물, 비타민, 가격]

min_cost = 500 * 15

# 먹어/ 안먹어로 접근
food_num = []
def eat(index, nums, p, f, s, v, c):
    global min_cost, food_num

    cur_nums = nums
    if index == N:
        cur_nutrient = [p, f, s, v]
        cur_cost = c
        for nutrient_index in range(4):
            if cur_nutrient[nutrient_index] < min_nutrient[nutrient_index]:
                return
        if min_cost > cur_cost:
            min_cost = cur_cost
            food_num = cur_nums
        return
    if foods[index][0] == 0 and foods[index][1] == 0 and foods[index][2] == 0 and foods[index][3] == 0:
        return eat(index+1, cur_nums, p, f, s, v, c)

    return eat(index+1, cur_nums+[index+1], p+foods[index][0], f+foods[index][1], s+foods[index][2], v+foods[index][3], c+foods[index][4]), eat(index+1, cur_nums, p, f, s, v, c)

eat(0, [],0, 0, 0, 0, 0)

if min_cost == 500*15:
    print(-1)
else:
    print(min_cost)
    print(*food_num)
