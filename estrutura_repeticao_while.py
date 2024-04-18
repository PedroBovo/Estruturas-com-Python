opcao = -1
while opcao!=0:
    saldo = 2000
    opcao = int(input("Digite [1] para saque e [2] para deposito e [0] para sair: "))
    if opcao == 1:
        valor = int(input("digite o valor que quer sacar: "))
        if valor <= saldo:
            print("saque realizado com sucesso")
        else:
            print("Valor insuficiente")
    elif opcao == 2:
        valor = int(input("Digite o valor de deposito: "))
        if(valor <= 0):
            print(f"impossivel depositar valor de {valor} reais ")
        else:
            print("Valor depositado com sucesso")
    elif opcao == 0:
        print("Obrigado volte sempre")

    opcao= int(input("valor inexistente tente novamente: "))