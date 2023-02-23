

""" 6. En sus propias palabras, qué son las funciones
preconstruidas y proporcione 2 ejemplos. """

print("\nSon funciones que ya vienen en los paquetes del lenguaje de programación " 
      "Python, solo debemos instanciarlas y tener en cuenta la finalidad de esa función preconstruida o predefinida")

print("\t1.Función sort\n\nUna de las funciones mas usadas en Python es .sort(), su funcionalidad es "
      "ordenar de manera ascendente o descendente una lista ya creada.")

print("Creamos una lista carros \ncarros = ['Ferrari', 'Lamborghini', 'Bugatti', 'Volvo']")

carros = ['Ferrari', 'Lamborghini', 'Bugatti', 'Volvo']
carros.sort()

print("Aplicarle sort de esta manera carros.sort(), nos ordenará la lista de la siguiente manera: \n", carros)

print("\n\t2. Función min\n\nRetorna la unidad minima dentro de una lista," 
      " usemos la lista ya creada de carros, siendo esta lista de cadenas "
      " de caracteres tomará la unidad minima en ordena alfabetico", min(carros))
