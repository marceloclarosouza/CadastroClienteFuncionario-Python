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
        super().__init__(nome, sobrenome, cpf, rg, sexo)##herança da super classe
        self.__saldo = saldo
        
        
cliente1 = Cliente('marcelo', "claro", 22233366656, 986574959, "M", 5000)
print(cliente1.imprimir_dados())