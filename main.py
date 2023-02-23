""" 8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

numero_uno = int(input("Ingresa el primer numero: "))
numero_dos = int(input("Ingresa el segundo numero :"))


if (numero_uno == numero_dos):       
   print("Los numeros son iguales")    
else:
    if(numero_uno>numero_dos):
      print("El primero es mayor")
    else:
       print("El segundo es mayor") 
