class Banco:
    def _init_(self):
        self.contas = {}

    def criar_conta(self, nome, saldo_inicial):
        conta_id = len(self.contas) + 1
        self.contas[conta_id] = {'nome': nome, 'saldo': saldo_inicial}
        return conta_id

    def exibir_saldo(self, conta_id):
        if conta_id in self.contas:
            return self.contas[conta_id]['saldo']
        return None

    def depositar(self, conta_id, valor):
        if conta_id in self.contas and valor > 0:
            self.contas[conta_id]['saldo'] += valor
            return True
        return False

    def sacar(self, conta_id, valor):
        if conta_id in self.contas and self.contas[conta_id]['saldo'] >= valor > 0:
            self.contas[conta_id]['saldo'] -= valor
            return True
        return False

    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem in self.contas and conta_destino in self.contas and valor > 0:
            saldo_origem = self.contas[conta_origem]['saldo']
            if saldo_origem >= valor:
                self.contas[conta_origem]['saldo'] -= valor
                self.contas[conta_destino]['saldo'] += valor
                return True
        return False

    def mostrar_menu(self):
        print("\nOpções disponíveis:")
        print("1. Exibir Saldo")
        print("2. Realizar Depósito")
        print("3. Realizar Saque")
        print("4. Realizar Transferência")
        print("5. Sair")

if _name_ == "_main_":
    banco = Banco()

    # Exemplo de uso:
    conta1 = banco.criar_conta("Cliente 1", 1000)
    conta2 = banco.criar_conta("Cliente 2", 500)

    while True:
        banco.mostrar_menu()
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            conta_id = int(input("Informe o número da conta: "))
            saldo = banco.exibir_saldo(conta_id)
            if saldo is not None:
                print(f"Saldo da conta {conta_id}: {saldo}")
            else:
                print("Conta não encontrada.")

        elif escolha == 2:
            conta_id = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do depósito: "))
            if banco.depositar(conta_id, valor):
                print("Depósito realizado com sucesso.")
            else:
                print("Depósito não pôde ser realizado.")

        elif escolha == 3:
            conta_id = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do saque: "))
            if banco.sacar(conta_id, valor):
                print("Saque realizado com sucesso.")
            else:
                print("Saque não pôde ser realizado.")

        elif escolha == 4:
            conta_origem = int(input("Informe o número da conta de origem: "))
            conta_destino = int(input("Informe o número da conta de destino: "))
            valor = float(input("Informe o valor da transferência: "))
            if banco.transferir(conta_origem, conta_destino, valor):
                print("Transferência realizada com sucesso.")
            else:
                print("Transferência não pôde ser realizada.")

        elif escolha == 5:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")