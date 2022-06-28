# Programa que calcula la diferencia entre dos varaibles y la almacena

def diferencia(xi, xf):
    y = xf-xi
    return y

xf = 0
xi = 0

while True:
    xf = float(input("\nIngrese un valor inicial: "))
    print(diferencia(xi, xf))
    xi = diferencia(xi, xf)
