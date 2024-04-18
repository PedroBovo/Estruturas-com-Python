opcao = int(input("Digite [1] para sacar ou [2] para ver extrato\n"))

if opcao == 1:
    saldo = 2000 
    saque = float(input("Digite o valor que quer sacar\n"))
    if saldo >= saque :
        print("Saque realizado com sucesso")
        valor_atual = saldo - saque
        
        print(f"saldo atual = {valor_atual}")
    else:
        print("saldo insuficiente")
elif opcao == 2:
    print(2000)
else:
    print("opcao invalida")