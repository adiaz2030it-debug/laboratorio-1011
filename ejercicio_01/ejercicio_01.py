"""
Ejercicio 1. Potencia recursiva

Implementa una función que calcule una potencia mediante multiplicaciones y
llamadas recursivas. Recibe una base numérica y un exponente entero no
negativo.

    def potencia(base, exponente):
        pass

En este ejercicio, cualquier base elevada a cero devuelve 1, incluido
potencia(0, 0).

Ejemplos

    potencia(2, 4)    # 16
    potencia(5, 0)    # 1
    potencia(-2, 3)   # -8
    potencia(0, 5)    # 0

Restricciones

- No utilices ciclos.
- No utilices ** ni pow().
- La solución debe ser recursiva.
"""


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuál es el caso base?
# El caso base es cuando exponente == 0, devolviendo 1.
#
# 2. ¿Qué argumento cambia en cada llamada?
# Cambia el argumento exponente, el cual disminuye en 1 en cada llamada (exponente - 1).
#
# 3. ¿Qué operación queda pendiente mientras se resuelve la llamada recursiva?
# Queda pendiente la multiplicación del valor de la base por el resultado que devuelva la llamada recursiva (base * ...).
#
# 4. Escribe las llamadas y los retornos de potencia(3, 3).
# Llamadas recursivas (pila de llamadas):
# - potencia(3, 3) llama a potencia(3, 2)
# - potencia(3, 2) llama a potencia(3, 1)
# - potencia(3, 1) llama a potencia(3, 0)
# - potencia(3, 0) alcanza el caso base y retorna 1
#
# Retornos acumulados:
# - potencia(3, 0) -> retorna 1
# - potencia(3, 1) -> 3 * 1 = 3 (retorna 3)
# - potencia(3, 2) -> 3 * 3 = 9 (retorna 9)
# - potencia(3, 3) -> 3 * 9 = 27 (retorna 27)
#

if __name__ == "__main__":
    print(potencia(2, 4))    # 16
    print(potencia(5, 0))    # 1
    print(potencia(-2, 3))   # -8
    print(potencia(0, 5))    # 0