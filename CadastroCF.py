""" Cadastro usando OOP com herança"""

class Pessoa:#super classe
    def __init__(self, nome, sobrenome, cpf, rg, sexo):
        """Retorna informacoes gerais das pessoas"""

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__rg = rg
        self.__sexo = sexo

    def imprimir_dados(self):
        """Imprimi as informações pessoais"""
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, rg, sexo, saldo):
        """Retorna as variaveis da superclasse + saldo"""
        super().__init__(nome, sobrenome, cpf, rg, sexo)##herança da super classe
        self.__saldo = saldo

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, rg, sexo, matricula):
        """Retorna as variaveis da superclasse + matricula"""
        super().__init__(nome, sobrenome, cpf, rg, sexo)
        self.__matricula = matricula

class Aposentado(Funcionario):##Herança multipla. Herda Funcionario diretamente e herda Pessoa indiretamemnte
    def __init__(self, nome, sobrenome, cpf, rg, sexo, matricula, saldo):
        super().__init__(nome, sobrenome, cpf, rg, sexo, matricula)
        self.__saldo = saldo



cliente1 = Cliente('marcelo', "claro", 22233366656, 986574959, "M", 5000)
print(cliente1.imprimir_dados())

funcionario1 = Funcionario("Gertrudez", "Python", 74185298754, 784596824, "F", "BB1569AP96")
print(funcionario1.imprimir_dados())

aposentado = Aposentado("Gertrudez", "Python", 74185298754, 784596824, "F", "BB1569AP96", 500)
print(aposentado.imprimir_dados())
