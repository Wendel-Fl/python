codigo = int(input("Digite o codigo do funcionario: "))
nome = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario do funcionario: "))
ativo = True

print("Código: %d" % codigo)
print("Nome: %s" % nome)
print("Salário: R$ %.2f" % salario)
print("Ativo: %r" % ativo)