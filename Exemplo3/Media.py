notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular a média
mediaFinal = (notaA + notaB) / 2

#verificar se o aluno foi aprovado
if mediaFinal >= 7.0:
   print("A média: %.1f - Aprovado" % mediaFinal)
else:
   print("A média: %.1f - Reprovado" % mediaFinal)