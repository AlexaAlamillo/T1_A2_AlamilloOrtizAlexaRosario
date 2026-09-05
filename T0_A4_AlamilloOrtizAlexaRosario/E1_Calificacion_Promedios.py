cantidad = int(input("Ingrese numero de calificaciones a promediar: "))

suma =0
reprobadas=0
aprobatorias=0
calificacion =0
for i in range(cantidad):
    calificacion=float(input(f"Ingrese calificacion{i+1}: "))
    suma = suma+ calificacion
    if(calificacion >= 70):
        aprobatorias+=1
    else:
        reprobadas +=1

promedio = suma/cantidad

print(f"Promedio: {suma}")
print(f"Materias aprobadas: {aprobatorias}")
print(f"Materias Reprobadas: {reprobadas}")        
            
       

    
