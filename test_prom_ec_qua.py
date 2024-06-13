# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:27:13 2024

@author: ferna
"""

import unittest
from promedio import promedio
from ec_cuadratica import resolver_ecuacion_cuadratica

class TestFunctions(unittest.TestCase):

    # Pruebas para la función promedio
    def test_promedio_notas(self):
        self.assertAlmostEqual(promedio([5, 7, 4]), 5.33333333333)
    
    # Pruebas para la función resolver_ecuacion_cuadratica
    def test_dos_soluciones_reales(self):
        self.assertAlmostEqual(resolver_ecuacion_cuadratica(1, -3, 2), [2.0, 1.0])
     
    def test_no_soluciones_reales(self):
        self.assertEqual(resolver_ecuacion_cuadratica(1, 0, 1), "No hay soluciones reales")
    
    
if __name__ == '__main__':
    unittest.main()
