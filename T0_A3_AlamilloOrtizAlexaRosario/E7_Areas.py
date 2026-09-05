print("--------MENU DDE OPCIONES----------")
print("1) Area de un rectangulo")
print("2) Area de un circulo ")
print("Ingrese la opcion: ")
opcion = input()

if(opcion == 1):
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura"))
    area=(base*altura)/2
    print(f"Area del triangulo : {area}")

if(opcion == 2):
    radio= float(input("Ingrese el radio : "))
    area_Circulo = 3.1416 * (radio*radio)
    print(f"El area del circulo es: {area_Circulo}")