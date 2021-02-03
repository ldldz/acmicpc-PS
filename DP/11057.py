n = int(input())
stair = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
tmp = [0] * 10

for _ in range(n - 1):
    for i in range(10):
        tmp[i] = sum(stair[0:i + 1])
    stair = tmp.copy()

print(sum(stair) % 10007)