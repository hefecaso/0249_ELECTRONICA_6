# Programa que regresará al stepper al Norte

import time

# Norte = 0° / 360°
# Oeste = 90°
# Sur = 180°
# Este = 270°

desplazado = int(input("¿Cuánto tiene desplazado el stepper? : "))
def Origen(desplazado):
    if 0<= desplazado <= 180:
        c12 = 360-(360-desplazado)
        return c12
    if 180 < desplazado <= 360:
        c34 = 360-desplazado
        return c34

##########
#def diferencia(xi, xf):
    #y = xf-xi
    #return y

xf = 0
xi = 0
y34 = xf-xi
y12 = xf-xi

##########

retorno = Origen(desplazado)
print("Regresando:", retorno)

while True:
    if 0<= desplazado <= 180:

        xi = retorno
        y12 = xf+xi
        xi = desplazado

        print("xf:", xf)
        print("y12:", y12)
        print("xi:", xi)
        time.sleep(3)

    if 180 < desplazado <= 360:
        xf = retorno
        y12 = xf-xi
        xi = xf

        print("xf:", xf)
        print("y12:", y12)
        print("xi:", xi)
        time.sleep(3)
