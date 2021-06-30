print ( "hola que tal estas")
print (__name__)    #da el nombre del modulo

# ver la variable y detectar el contexto en que se ejecuta el codigo
numero= 324223
a=3
b=4
c=5

if __name__ == "__main__":
    print ("me gusta ser un modulo")
    
else:
    print ("me encanta ser un modulo")


#funcion sumar

numero=8
def sumar (a,b):
    print("estos es una suma")
    return a + b

def producto(a,b):
    print ("eso es una multiplicacion")
    return a*b

if __name__ == "__main__":
    print ("me gusta ser un modulo")
    print (sumar (5,5))
    print (producto(5,5))
    
else:
    print ("me encanta ser un modulo")
    
    
