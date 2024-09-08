class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque_valor = 500

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
        else:
            self.saldo += valor
            self.extrato.append(f"Depósito: +${valor:.2f}")
            print(f"Depósito de ${valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Erro: Limite de saques diários alcançado.")
        elif valor > self.limite_saque_valor:
            print(f"Erro: O valor máximo permitido para saque é de ${self.limite_saque_valor:.2f}.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
        elif valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: -${valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de ${valor:.2f} realizado com sucesso!")

    def visualizar_extrato(self):
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print("Extrato:")
            for movimento in self.extrato:
                print(movimento)
            print(f"Saldo atual: ${self.saldo:.2f}")

    def reiniciar_saques_diarios(self):
        self.saques_diarios = 0


# Exemplo de uso do sistema bancário
banco = Banco()

while True:
    print("\nBem-vindo ao sistema bancário! Selecione uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        banco.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        banco.sacar(valor)
    elif opcao == '3':
        banco.visualizar_extrato()
    elif opcao == '4':
        print("Obrigado por utilizar nosso sistema bancário!")
        break
    else:
        print("Opção inválida. Tente novamente.")
