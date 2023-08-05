def imprimirConjunto(conjunto):
    if len(conjunto) == 0:
        print('{}')
    else:
        print(conjunto)

cantidadA = int(input("¿Cuantos elementos para el conjunto A?"))
conjuntoA = set()

for i in range(cantidadA):
    elementoA = int(input("Escribe un elemento para la lista A: "))
    conjuntoA.add(elementoA)

cantidadB = int(input("¿Cuantos elementos para el conjunto B?"))
conjuntoB = set()

for i in range(cantidadB):
    elementoB = int(input("Escribe un elemento para la lista B: "))
    conjuntoB.add(elementoB)

print("A = ", end="")
imprimirConjunto(conjuntoA)
print("B = ", end="")
imprimirConjunto(conjuntoA)

print ("Selecione una operacion")
print ("1. Unión")
print ("2. Intersección")
print ("3. Diferencia")
print ("4. Diferancia simétrica")
opcion = int(input("Elige una opción: "))

if opcion == 1:
    a = conjuntoA|conjuntoB
    imprimirConjunto(a)
    print ("El cardinal es: ", len(a))
elif opcion == 2:
    b = conjuntoA & conjuntoB 
    imprimirConjunto(b)
    print ("El cardinal es: ", len(b))
elif opcion == 3:
    c = conjuntoA - conjuntoB
    imprimirConjunto(c)
    print ("El cardinal es: ", len(c))
elif opcion == 4:
    d = conjuntoA ^ conjuntoB
    imprimirConjunto(d)
    print ("El cardinal es: ", len(d))
