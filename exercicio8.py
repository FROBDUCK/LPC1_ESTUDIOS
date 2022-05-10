for i in range(0, 5):
  nome = str(input('Digite o nome da pessoa:\n'))

  nomes.append(nome)
  altura = float(input('Digite a altura da respectiva pessoa:\n'))

  alturas.append(altura)

nomes.reverse()
alturas.reverse()
print('A ordem inversa dos nomes é: ' + str(nomes))
print('A ordem inversa das alturas é: ' + str(alturas))
