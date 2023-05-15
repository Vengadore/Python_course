from .estructura import *
import math

def rectangular(complejo):
    return f"{complejo[0]} + {complejo[1]}j"

#def polar(*args):
#    raise NotImplementedError("La función 'polar' no está implementada")

def polar(complejo):
    modulo = round((complejo[0]**2 + complejo[1]**2)**0.5,3)
    angulo = round(math.degrees(math.atan(complejo[1]/complejo[0])),3)

    return f"{modulo} {angulo}°"