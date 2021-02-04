def solve():
    n = int(input())
    sticker = []
    for i in range(2): sticker += list(map(int, input().split()))
    print(sticker) 


t = int(input())
for _ in range(t): solve()