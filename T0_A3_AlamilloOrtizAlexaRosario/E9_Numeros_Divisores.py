print("Ingrese un numero: ")
a= int(input())
print("Ingrese otro numero: ")
b=int(input())
c = a % b
d= b % a 
if(c ==0 and d ==0 ):
    print(f"{a} y {b} son divisores el uno del otro")
else:
    print(f"{a} y {b} no son divisores el uno del otro")    