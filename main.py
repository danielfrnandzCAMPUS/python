class Camper:
    def __init__(self, nombre, cedula, edad):
        self.name = nombre
        self.ident = cedula
        self.age = edad

    def __str__(self) -> str:
        return 'Cedula: {}\nNombre: {}\nEdad: {}'.format(self.ident, self.name, self.age)
    

listaArtemis=[]
listaSputnik=[]

def imprimirListaArtemis(lista):
    for i in lista:
        print(i)

def borrarCamper(lista):
    delete = input("Ingresa la cedula del camper a eliminar: ")
    for i in lista:
        if delete == i.ident:
            lista.remove(i)

def buscarCamper(lista):
    search = input("Ingresa la cedula del camper a buscar: ")
    for i in lista:
        if search == i.ident:
            print(i)

def ordenarCamper(lista):
    ordenar = sorted(lista, key= lambda cam: cam.name)
    for i in ordenar:
        print(i)


i=0
while i==0:
    print("-----------MENÚ PRINCIPAL-----------"
    "\n1. CREAR GRUPO ARTEMIS"
    "\n1.1 LISTAR CAMPERS DE ARTEMIS "
    "\n1.2 AGREGAR CAMPERS DE ARTEMIS"
    "\n1.3 ELIMINAR CAMPERS DE ARTEMIS"
    "\n1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS"
    "\n1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS"
    "\n2. CREAR GRUPO SPUTNIK"
    "\n2.1 LISTAR CAMPERS DE SPUTNIK "
    "\n2.2 AGREGAR CAMPERS DE SPUTNIK"
    "\n2.3 ELIMINAR CAMPERS DE SPUTNIK"
    "\n2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK"
    "\n2.5 BUSCAR CAMPER EN LISTA DE ARTEMIS"
    "\n3. Salir")
    
    opcion = float(input("Digita la opción:"))
    
    if opcion == 1.1:
        print("1.1 LISTAR CAMPERS DE ARTEMIS")
        imprimirListaArtemis(listaArtemis)
    elif opcion == 1.2:
        print("1.2 AGREGAR CAMPERS DE ARTEMIS")
        nom = input("Digita el nombre del Camper: ")
        ced = input("Digita la cedula del Camper: ")     
        ed = input("Digita la edad del camper: ")   
        camp = Camper(nom, ced, ed)
        listaArtemis.append(camp)
        print("Camper guardado con exito")
    elif opcion == 1.3:
        print("1.3 ELIMINAR CAMPERS DE ARTEMIS")        
        borrarCamper(listaArtemis)
    elif opcion == 1.4:
        print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
        ordenarCamper(listaArtemis)
    elif opcion == 1.5:
        print("1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS")
        buscarCamper(listaArtemis)
    elif opcion == 2.1:
        print("1.1 LISTAR CAMPERS DE SPUTNIK")
        imprimirListaArtemis(listaSputnik)
    elif opcion == 2.2:
        print("1.2 AGREGAR CAMPERS DE SPUTNIK")
        nom = input("Digita el nombre del Camper: ")
        ced = input("Digita la cedula del Camper: ")     
        ed = input("Digita la edad del camper: ")   
        camp = Camper(nom, ced, ed)
        listaSputnik.append(camp)
        print("Camper guardado con exito")
    elif opcion == 2.3:
        print("1.3 ELIMINAR CAMPERS DE SPUTNIK")        
        borrarCamper(listaSputnik)
    elif opcion == 2.4:
        print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
        ordenarCamper(listaSputnik)
    elif opcion == 2.5:
        print("1.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")
        buscarCamper(listaSputnik)        
    elif opcion == 3:
        exit()
    else:
        print("Opción invalida")