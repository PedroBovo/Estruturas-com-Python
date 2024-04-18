saldo = 200
saque = 300
status = "Sucesso" if saque <= saldo else "Falha"

print(f"{status} ao realizar o saque")