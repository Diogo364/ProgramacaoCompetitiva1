columns = int(input())
caixas = list(map(int, input().split(" ")))
print(' '.join(map(str, sorted(caixas))))

