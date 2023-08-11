def union(C1, C2):
    return C1|C2
def Intersecccion(C1, C2):
    return C1&C2
def Diferencia(C1, C2):
    return C1-C2
def  DiferanciaSimetrica(C1, C2):
    return C1^C2

A = set()
for i in range(1, 26):
    if i %2 == 1:
        A.add(i)
        
B = set()
for i in range(6, 20):
        B.add(i)
        
C = {1, 4, 7, 8, 12, 16, 18, 21}
    
D = {2, 3, 5, 37,7, 41, 11, 43, 13, 47, 17, 18, 19, 23, 29, 31, 37, 41, 43, 47}

op1 = Intersecccion(A, DiferanciaSimetrica(B, D))
op2 = union(Intersecccion(B, C), D)
op3 = Diferencia(union(A,C), B)
op4 = DiferanciaSimetrica(Diferencia(B, C), Intersecccion(A, C))

print(f"El conjunto A es: {A}")
print(f"El conjunto B es: {B}")
print(f"El conjunto C es: {C}")
print(f"El conjunto D es: {D}")

print(f"Operacion 1: {op1}")
print(f"Operacion 2: {op2}")
print(f"Operacion 3: {op3}")
print(f"Operacion 4: {op4}")