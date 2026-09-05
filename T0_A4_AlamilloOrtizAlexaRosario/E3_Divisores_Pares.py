print("Ingrese un numero: ")
numero = int(input())

print("Los divisopres pares son: ")

for i in range(1, numero+1):
    if(numero %i==0 and numero%2==0):
        print(i)