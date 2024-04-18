texto = input("digite um texto")
vogais = "AEIOU"
#ultilizando um iteravel
for letra in texto:
    if(letra.upper() in vogais):
        print(letra, end=" ")
else:
    print("\nFim do programa")


print() 
#ultilizando biult-in range
for numero in range(0, 11):
    for i in range(0,11):
        print(f"{numero} * {i} = ", (numero*i))
        