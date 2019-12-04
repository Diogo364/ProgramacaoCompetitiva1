a, b = list(map(int, input().split()))
contador = 0
while a <= b:
    contador += 1
    a *= 3
    b *= 2
print(contador)