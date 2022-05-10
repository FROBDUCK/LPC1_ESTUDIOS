numeros = []
for i in range(0, 5):
  addnumero = int(input('Digite o número a ser adicionado:\n'))
  numeros.append(addnumero)

print(numeros)
print('A soma de todos os numeros é : ' + str(sum(numeros)))

multi = 1
for i in range(0, len(numeros)):
  multi *= numeros[i]

print('A multiplicação de todos os números é: ' + str(multi))