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





