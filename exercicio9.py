numeros = []
for i in range(0, 10):
  addnumero = int(input('Digite o número a ser adicionado:\n'))
  numeros.append(addnumero)

quadrado = 0
for i in range(0, len(numeros)):
  quadrado += (numeros[i] ** 2)

print('A soma dos quadrados dos elementos é: ' + str(quadrado))