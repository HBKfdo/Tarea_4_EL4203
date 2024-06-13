# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:16:27 2024

@author: HBKfdo
"""
def promedio(notas: list)-> float:
    """Función que calcula el promedio de una lista de notas."""
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    for nota in notas:
        if nota < 1 or nota > 7:
            raise ValueError("La nota debe estar entre 1 y 7.")
    return sum(notas) / len(notas)
