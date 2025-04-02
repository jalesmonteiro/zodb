class ContaBancaria:
    def __init__(self, titular, saldo_inicial, numero_conta):
        self.titular = titular # Atributo público: acessível de qualquer lugar
        self._saldo = saldo_inicial # Atributo protegido: convenção para uso interno ou em subclasses
        self.__numero_conta = numero_conta # Atributo privado: nome modificado para dificultar o acesso externo direto

    # Método público: acessível de qualquer lugar
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self._saldo

    # Método protegido: convenção para uso interno ou em subclasses
    def _gerar_extrato(self):
        return f"Extrato da conta {self.__numero_conta} (Titular: {self.titular}): Saldo atual R$ {self._saldo:.2f}"

    def exibir_extrato(self):
        print(self._gerar_extrato())

    # Método privado: nome modificado para dificultar o acesso externo direto
    def __obter_numero_conta_interno(self):
        return self.__numero_conta

    # Método público que pode fornecer acesso controlado ao atributo privado
    def mostrar_numero_conta_parcial(self):
        return f"Número da conta: ****{self.__numero_conta[-4:]}"

# Exemplo de uso da classe ContaBancaria
print("--- Exemplo da Classe ContaBancaria ---")
conta = ContaBancaria("João", 1000.00, "12345-6")

print(f"Titular da conta: {conta.titular}") # Acesso ao atributo público

conta.depositar(500.00)
print(f"Saldo atual: R$ {conta.consultar_saldo():.2f}")

conta.sacar(200.00)
print(f"Saldo atual: R$ {conta.consultar_saldo():.2f}")

# Acessando o atributo protegido (funciona, mas é desencorajado fora da classe/subclasses)
# print(f"Saldo (acesso direto ao protegido): R$ {conta._saldo:.2f}")

conta.exibir_extrato() # Acesso ao método protegido através de um método público

print(conta.mostrar_numero_conta_parcial()) # Acesso controlado ao atributo privado

# Tentando acessar o atributo privado diretamente (gera um AttributeError)
# print(f"Número da conta (acesso direto ao privado): {conta.__numero_conta}")

# Acessando o atributo privado usando o 'name mangling' (não recomendado)
# print(f"Número da conta (acesso 'name mangling'): {conta._ContaBancaria__numero_conta}")