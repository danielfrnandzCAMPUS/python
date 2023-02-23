class Atleta:
    def __init__(self, nombre, marca):
        self.name = nombre
        self.mark = marca
    
    def __str__(self) -> str:
        return 'Nombre: {}, Marca: {}'.format(self.name, self.mark)

listaAtletas=[]
record = float(15.50)

def imprimirLista(lista):
    for i in lista:
        print(i)

def ganadora(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i): 
            if lista[j].mark < lista[j+1].mark:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    if lista[0].mark > record:
        print(f"Ganadora de Oro : ", lista[0], " ,recibe 500 millones por romper el record")
    else:
        print(f"Ganadora de Oro : ", lista[0], " , no recibe bonificación")

i=0
while i==0:
    print("-----------MENÚ PRINCIPAL-----------"
    "\n1. REGISTRAR ATLETA"
    "\n2. LISTADO DE ATLETAS PARTICIPANTES"
    "\n3. ATLETA GANADORA ORO")

    opcion = int(input("Digita una opción:  "))
    if opcion == 1:
        print("1. REGISTRO DE ATLETA")
        nom = input("Nombre del atleta: ")
        mar = float(input("Digita la marca del atleta: "))
        atl = Atleta(nom,mar)
        listaAtletas.append(atl)
        print("Atleta guardado")
    elif opcion == 2:
        print("2. LISTADO DE ATLETAS PARTICIPANTES")
        imprimirLista(listaAtletas)
    elif opcion == 3:
        print("3. ATLETA GANADORA ORO")
        ganadora(listaAtletas)
    else:
        print("Opcion invalida")



