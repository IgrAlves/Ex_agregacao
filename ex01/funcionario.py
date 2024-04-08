class Funcionario:

    def __init__(self, nome, codigo, idade):
        self.nome = nome
        self.codigo = codigo
        self.idade = idade

    def inserir_departamento(self, departamento):
        self.departamento = departamento