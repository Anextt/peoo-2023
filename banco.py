#exibe uma mensagem para pedir o cartão e 
#em seguida as opções
cart = input("Inserir Seu Cartão De Crédito: ()")
print(cart["Saque"])
print(cart["Depósito"])
print(cart["Transferência"])
print(cart["Bloqueio"])
print(cart["Saque"])

#verifica o status do cartão
if cart < 1:
    print("Cartão Recusado, Insira-o Novamente")
else:
    print ()