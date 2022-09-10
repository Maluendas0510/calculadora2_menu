# calculadora con menu
from math import log
print("----------------------------")
print("-----calculadora-menu:----")

#input
bandera = False
x= float(input("dame el valor del numero x:"))
y=float(input("dame el valor del numero y"))

print("\nDame la opcion que deseas realizar:\n")
# se despliega el menu para seleccionar la opcion que deseas realizar:
print("1.sumar(el primero mas el segundo)")
print("2.restar(el primero menos el segundo)")
print("3.multiplicar(el primero por el segundo)")
print("4.dividir(el primero ala potencia del segundo)")
print(".sumar(el primero mas el segundo)")
 
opcion=int(input("\nDame la opcion:"))

#processing
if (opcion ==1):
    z = x+y
    print(x,"+",y)
elif (opcion ==2):
    z =x-y 
    print(x,"-",y)
elif (opcion ==3):
    z=x*y
    print(x,"*",y)
elif (opcion == 4 and y!=0):
    z=x/y
    print(x,"/",y)
elif (opcion ==4 and y==0):
    print("el denominador es igual a cero y")
    print("no se puede realizar la division")
    bandera=True
elif (opcion==5):
    z= pow(x,y)
    print(x,"^",y)
elif (opcion==6 and x>0):
    z=log(x)
    print("logaritmo de",x)
elif(opcion==6 and x<=0):
    print("el valor de x es <= a cero")
    print("no se puede calcular el logaritmo")
    bandera=True
else:
    print("opcion no valida")
    
# se escribe el resultado con otra condicion
if (opcion<7 and bandera == False):
    print("resultado=",z)
    
 # fin   
            
    