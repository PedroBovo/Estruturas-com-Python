
while True:
    numero = int(input("Digite um numero: "))
    if numero == 10:
        break

for i in range(101):
    if i % 2 == 0:
        continue
    print(i)
