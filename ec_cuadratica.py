# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:18:59 2024

@author: HBKfdo
"""

import math

def resolver_ecuacion_cuadratica(a: float, b: float , c: float) -> list:
    # Calcula el discriminante
    discriminante = b**2 - 4*a*c
    
    # Si el discriminante es negativo, no hay soluciones reales
    if discriminante < 0:
        return "No hay soluciones reales"
    
    # Calcula las dos soluciones
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    # Devuelve las soluciones
    return [x1, x2]
