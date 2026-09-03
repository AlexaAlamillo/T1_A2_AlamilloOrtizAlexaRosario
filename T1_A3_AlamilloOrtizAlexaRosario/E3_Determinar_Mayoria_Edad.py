anio= int(input("Ingrese su anio de nacimiento: "))
fecha = input("Ingrese su dia y mes de nacimiento: ")


edad = 2026-anio
print(f"Su fecha de nacimiento es {fecha} {anio}")
if(edad>=18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")    