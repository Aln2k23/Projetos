class Pessoa:
    def __init__(self, nome_completo, cpf, data_nascimento) -> None:
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Cliente(Pessoa):
    def __init__(self, nome_completo, cpf, data_nascimento, telefone, email) -> None:
        super().__init__(nome_completo, cpf, data_nascimento)
        self.telefone = telefone
        self.email = email

class Funcionario(Pessoa):
    def __init__(self, nome_completo, cpf, data_nascimento, telefone, email, cep) -> None:
        super().__init__(nome_completo, cpf, data_nascimento)
        self.telefone = telefone
        self.email = email
        self.cep = cep
        self.salario = None
    
    def inserir_salario_funcionario(self, salario):
        self.salario = salario

alan = Pessoa('Alan Pereira Cavalcante', '58165977873', '16/03/2003')

