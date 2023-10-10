#exibe uma lista para que o usuário selecione o que dedseja

print("====================$====================")
transacao = ["Saque, Deposito, Transferência, Bloqueio"]
print(transacao)

info = input("insira a trnsação desejada: ")

cart = input("Inserir número do Cartão De Crédito: ")

#verifica o status do cartão
if cart != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    print("Cartão Recusado, Insira-o Novamente")
else:
    print ("_")