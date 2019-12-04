contador = 0
for _ in range(int(input())):
    x, y, z = list(map(int, input().split()))
    if x + y + z > 1:
        contador += 1
print(contador)