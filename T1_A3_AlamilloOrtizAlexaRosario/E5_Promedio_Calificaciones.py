print("Promedio de calificaciones")

cali_1 = int(input("Ingrese calificacion 1: "))
cali_2 = int(input("Ingrese calificacion 2: "))
cali_3 = int(input("Ingrese calificacion 3: "))
cali_4 = int(input("Ingrese calificacion 4: "))
cali_5 = int(input("Ingrese calificacion 5: "))
suma= cali_1 + cali_2 +cali_3 +cali_4 + cali_5

promedio = suma/5

print(f"Su promedio es : {promedio}")

if(promedio >=70):
    print("Su promedio es aprobatorio")
else: 
    print("Su promedio no es aprobatorio")    
