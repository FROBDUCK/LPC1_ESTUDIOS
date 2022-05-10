#1
vetor = [1, 2, 3,4, 5]
print(vetor)
#2
v = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
v.reverse()
print(v)
#3
notas = [5, 7, 4, 10]
print(notas)
media = sum(notas) / 4
print('media: ',media)

#4
v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
contador = 0
for va in v:
    if va != 'a' and 'e' and 'i' and 'o' and 'u':
        contador += 1

        print(va)

print(contador)
#5
v=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
impar=[]
par=[]

for numero in range(0,20):
    if v[numero] % 2 == 0:
        par.append(v[numero])
    else: impar.append(v[numero])

print("todos os numeros: " +str(v))
print("numeros impar: " +str(impar))
print("numeros pares:" +str(par))
#6
listaNotas = []
notasAluno = []
print ('Notas dos Alunos')
for i in range(10):
 	media = 0
 	notasAluno = []
 	print ('Aluno: ' + str(i + 1))
 	for j in range(4):
 		notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
 		media += notasAluno[j]
 		print (media)
 	media = media/4
 	listaNotas.append(media)

#7
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

#8

for i in range(0, 5):
  nome = str(input('Digite o nome da pessoa:\n'))

  nomes.append(nome)
  altura = float(input('Digite a altura da respectiva pessoa:\n'))

  alturas.append(altura)

nomes.reverse()
alturas.reverse()
print('A ordem inversa dos nomes é: ' + str(nomes))
print('A ordem inversa das alturas é: ' + str(alturas))


#9
numeros = []
for i in range(0, 10):
  addnumero = int(input('Digite o número a ser adicionado:\n'))
  numeros.append(addnumero)

quadrado = 0
for i in range(0, len(numeros)):
  quadrado += (numeros[i] ** 2)

print('A soma dos quadrados dos elementos é: ' + str(quadrado))

#10
numbers = []
characters = []

for i in range(0, 10):
  addNumber = int(input('Digite um valor inteiro para ser adicionado:\n'))
  numbers.append(addNumber)

for i in range(0, 10):
  character = str(input('Digite um caracter para ser adicionado:\n'))
  while(len(character) != 1):
    character = str(input('Por favor, digite apenas um caracter:\n'))
  else:
    characters.append(character)

group = []
for i in range(0, len(numbers)):
  group.insert(len(group), numbers[i])
  group.insert(len(group), characters[i])

print(group)