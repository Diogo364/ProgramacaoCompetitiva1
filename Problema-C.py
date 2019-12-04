word = input()
qtdLower = 0
for letter in word:
    if letter.islower():
        qtdLower += 1
if qtdLower >= (len(word) - qtdLower):
    print(word.lower())
else:
    print(word.upper())
