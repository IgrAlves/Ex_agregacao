from departamento import Departamento
from funcionario import Funcionario

nome_funcionario = str(input("Digitar nome do funcionário: "))
codigo_funcionario = int(input("Digitar código do funcionário: "))
idade_funcionario = int(input("Digitar idade do funcionário: "))
nomeDepartamento = str(input("Digitar nome do departamento: "))
codigoDepartamento = int(input("Digitar código departamento: "))

funcionario = Funcionario(nome_funcionario, codigo_funcionario, idade_funcionario)
departamento = Departamento(nomeDepartamento, codigoDepartamento)

funcionario.inserir_departamento(departamento)
print("Nome do funcionário: ", funcionario.nome)
print("Código do funcionário: ", funcionario.codigo)
print("Idade do funcionario: ", funcionario.idade)
print("Nome Departamento: ", departamento.nome_departamento)
print("Codigo Departamento: ", departamento.codigo_departamento)