cadena = input("Ingrese una frase o palabra : ")
invertida = " "

for i in range(len(cadena)-1,-1,-1):
    invertida += cadena[i]
 
print(f"La palabra invertida es: {invertida}")   
