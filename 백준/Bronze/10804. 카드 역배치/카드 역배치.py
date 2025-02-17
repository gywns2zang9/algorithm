#카드 역배치
cards = list(i for i in range(1, 21))

for _ in range(10):
    A, B = map(int, input().split())
    gap = B-A
    for i in range(gap//2+1):
        cards[A+i-1], cards[B-i-1] = cards[B-i-1], cards[A+i-1]
for j in range(20):
    print(cards[j], end=" ")