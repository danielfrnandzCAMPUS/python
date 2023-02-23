
""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

actual = 2023
nombre = input("Ingresa el nombre del empleado: ")
apellidos = input("Ingresa los apellidos del empleado: ")
telefono = input("Ingresa el telefono del empleado: ")
edad = int(input("Ingresa la edad del empleado: "))
ingreso = int(input("Ingresa el año de ingreso del empleado a la empresa:"))

antiguedad = actual - ingreso

if (antiguedad<0 or edad <0):
    print("Fecha de ingreso no puede ser mayor al año actual")
else:
    print(f"\tDatos del Empleado: \nNombre: {nombre} \nApellidos: {apellidos}")
    print(f"Telefono: {telefono} \nEdad: {edad}")
    print(f"La antigüedad del empleado es: {antiguedad} años")
