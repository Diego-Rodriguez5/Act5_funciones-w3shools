print("Ejemplo de funciones:")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"Chat {mensa}")
    
def ellacontesta(mensa):
    print(f"Chat de ella: {mensa}")
    
def escribenombre(ap,n):
    print(f"Su nombre completo es: {n} {ap}")
    
def suma(a,b):
    s=a+b
    return s

def resta(c,d):
    s=c-d
    return s

def multiplicaion(e,f):
    s=e*f
    return s

def division(g,h):
    s=g/h
    return s
    
# Llamadas a funciones
hola()
chat("Que bonita estas")
ellacontesta("Gracias")
escribenombre("Rodriguez","Diego")

print("Operacione suma")
c1=int(input("Ingresa un numero:"))
c2=int(input("Ingresa un numero:"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacione resta")
c3=int(input("Ingresa un numero:"))
c4=int(input("Ingresa un numero:"))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacione multiplicacion")
c5=int(input("Ingresa un numero:"))
c6=int(input("Ingresa un numero:"))
damemultiplicacion=multiplicaion(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damemultiplicacion}")

print("Operacione division")
c7=int(input("Ingresa un numero:"))
c8=int(input("Ingresa un numero:"))
damedivision=division(c7,c8)
print(f"La division de {c7} / {c8} = {damedivision}")
