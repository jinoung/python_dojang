#x, y = [input() for _ in range(2)]
x = map(float, input().split())
y = map(float, input().split())
print(dict(zip(x, y)))

