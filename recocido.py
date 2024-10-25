import numpy as np
import math

def objetivo(x):
    return x**2 + 4*np.sin(5*x)

def generar_vecino(x_actual):
    return x_actual + np.random.uniform(-0.1, 0.1)

def recocido_simulado(temperatura_inicial, enfriamiento, max_iter):
    solucion_actual = np.random.uniform(-10, 10)
    valor_actual = objetivo(solucion_actual)
    
    mejor_solucion = solucion_actual
    mejor_valor = valor_actual

    temperatura = temperatura_inicial

    for i in range(max_iter):
        nueva_solucion = generar_vecino(solucion_actual)
        nuevo_valor = objetivo(nueva_solucion)

        if nuevo_valor < valor_actual or np.random.uniform(0, 1) < math.exp(-(nuevo_valor - valor_actual) / temperatura):
            solucion_actual = nueva_solucion
            valor_actual = nuevo_valor
        
        if nuevo_valor < mejor_valor:
            mejor_solucion = nueva_solucion
            mejor_valor = nuevo_valor

        temperatura *= enfriamiento

    return mejor_solucion, mejor_valor

temperatura_inicial = 1000
enfriamiento = 0.95
max_iter = 5000

mejor_solucion, mejor_valor = recocido_simulado(temperatura_inicial, enfriamiento, max_iter)

print(f"Mejor solución: {mejor_solucion}, con valor: {mejor_valor}")