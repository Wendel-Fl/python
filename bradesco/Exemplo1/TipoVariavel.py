Código = 10
salario = 1500.00
nome = 'José'
situacao = True

tipo = type(salario)

print(salario)
print(tipo)
print("Código:", Código, "Nome:", nome, "O salario atual é de: R$", salario)
print("Código: %d, Nome: %s, O salário atual é de: R$ %.2f" % (Código, nome, salario))
print("Código: {0}, nome: {1}, salário: {2}".format(Código, nome, salario))
print("Código: {Código}, nome: {nome}, salário: {salario}".format(Código=Código, nome=nome, salario=salario))
print("Código: " + str(Código) + ", Nome: " + nome + ", O salário atual é de: R$ " + str(salario))