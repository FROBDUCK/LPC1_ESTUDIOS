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