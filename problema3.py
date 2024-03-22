#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
class ArbolTrinario:
    def __init__(self, numero):
        self.numero = numero
        self.izquierda = None
        self.centro = []
        self.derecha = None

def InsertarEnArbolTrinario(arbol, numero):
    if arbol is None:
        return ArbolTrinario(numero)
    if numero < arbol.numero:
        arbol.izquierda = InsertarEnArbolTrinario(arbol.izquierda, numero)
    elif numero > arbol.numero:
        arbol.derecha = InsertarEnArbolTrinario(arbol.derecha, numero)
    else:
        arbol.centro.append([])
    return arbol

def imprimirArbol(arbol):
    if arbol:
        print("[", arbol.numero, end="")
        imprimirArbol(arbol.izquierda)
        if arbol.centro:
            print(", []", end="")
            for centro in arbol.centro:
                imprimirArbol(centro)
        imprimirArbol(arbol.derecha)
        print("]", end="")

def leer_numeros():
    numeros = input().split()
    return [int(numero) for numero in numeros]

numeros = leer_numeros()
arbol = None
for numero in numeros:
    arbol = InsertarEnArbolTrinario(arbol, numero)

print("Arbol trinario:")
imprimirArbol(arbol)
