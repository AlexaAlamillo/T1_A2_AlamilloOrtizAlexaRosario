cantidad_seg= float(input("Ingrese la cantidad en segundos: "))
min = 60 
hora = 3600


print("===========CONVERSIONES DE TIEMPO=======")

horas =cantidad_seg // hora
print(f"Horas: {horas}")


restante_horas = cantidad_seg%hora
cantidad_Min = restante_horas //min
print(f"Minutos {cantidad_Min}")
restante_min = restante_horas%min
print(f"Segundos restantes: {restante_min}")
