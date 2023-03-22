while True:
    print('Ingresar digitos(15)')
    cuenta=input()
    if len(cuenta)==15:
        break
sumIm=0
sumP=0
cont=0
cuentaArray=[]
for i in range(1,len(cuenta)+1,1):
    cuentaArray.append(int(cuenta[i-1:i]))
print(cuentaArray)

for i in range(0,len(cuenta),2):
    sumIm+=cuentaArray[i]
    if i < 14:
        sumP+=cuentaArray[i+1]
    if cuentaArray[i]>=5:
        cont+=1
sumIm*=2
print(sumIm)
sumIm-=(cont*9)
print('Operaciones Impares:',sumIm)
print('Operaciones Pares:',sumP)

sumT=sumIm+sumP
print('Suma de las Operaciones:',sumT)
resultado=0
while sumT%10!=0:
    resultado+=1
    sumT+=1
print('Resultado:',resultado)