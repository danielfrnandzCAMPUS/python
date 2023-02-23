

""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """


estratos = [1,233,291,496,583,700,700]
mes = input("Ingresa el mes de consumo: ")
valor_kw = int(input("Ingresa el valor por cada kw: "))
estrato = int(input("Ingresa el estrato de la casa ( 1 a 6 ): "))
consumo_kw = int(input("Ingresa los kw consumidos en el mes: "))

total = consumo_kw * valor_kw *estratos[estrato]


print(f"El total de la factura en el mes de {mes} fue de {total}, con consumo de {consumo_kw} con valor de {valor_kw} de cada Kw para el estrato {estrato}")
