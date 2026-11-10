"""
Ejercicio 2. Contar valores a partir de un límite

Un sensor registra mediciones numéricas en una lista. Necesitamos saber cuántas
son mayores o iguales que un límite.

Implementa una versión recursiva que cuente únicamente desde la posición i
hasta el final. Puedes asumir que 0 <= i <= len(valores).

    def contar_desde_limite(valores, limite, i=0):
        pass

Implementa también una versión iterativa que procese la lista completa:

    def contar_desde_limite_iterativo(valores, limite):
        pass

Ejemplos

    contar_desde_limite([12, 5, 18, 7, 10], 10)      # 3
    contar_desde_limite([12, 5, 18, 7, 10], 10, 2)   # 2
    contar_desde_limite([], 10)                      # 0
    contar_desde_limite([4, 4, 4], 4)                # 3

Restricciones

- La versión recursiva no puede utilizar ciclos ni cortes.
- La versión iterativa debe utilizar un ciclo.
- No construyas una lista auxiliar con los valores que cumplen la condición.
- Ninguna versión debe modificar la lista original.
"""


def contar_desde_limite(valores, limite, i=0):
    """Cuenta desde la posición i hasta el final. Se asume 0 <= i <= len(valores)."""
    if i == len(valores):
        return 0
    cumple = 1 if valores[i] >= limite else 0
    return cumple + contar_desde_limite(valores, limite, i + 1)


def contar_desde_limite_iterativo(valores, limite):
    """Cuenta en la lista completa usando un ciclo."""
    contador = 0
    for valor in valores:
        if valor >= limite:
            contador += 1
    return contador


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué representa el parámetro i?
# Representa el índice o posición actual de la lista a partir del cual se iniciará la revisión de los elementos.
#
# 2. ¿Qué cantidad disminuye a medida que aumenta i?
# Disminuye la cantidad de elementos restantes por procesar en la lista (es decir, len(valores) - i).
#
# 3. ¿Qué devuelve una llamada si el elemento actual no cumple la condición?
# Devuelve 0 + contar_desde_limite(valores, limite, i + 1), lo que equivale simplemente al resultado de la llamada recursiva para el siguiente elemento.
#
# 4. ¿Qué diferencia hay entre la información pendiente de la versión
#    recursiva y la de la iterativa?
# En la versión recursiva, la suma del elemento actual queda pendiente en la pila de llamadas (stack) hasta que el caso base responde. En la versión iterativa, no hay operaciones pendientes guardadas en memoria; la cuenta se acumula inmediatamente en una variable de estado (contador) dentro de cada iteración del ciclo.
#


if __name__ == "__main__":
    print(contar_desde_limite([12, 5, 18, 7, 10], 10))      # 3
    print(contar_desde_limite([12, 5, 18, 7, 10], 10, 2))   # 2
    print(contar_desde_limite([], 10))                      # 0
    print(contar_desde_limite([4, 4, 4], 4))                # 3

    print(contar_desde_limite_iterativo([12, 5, 18, 7, 10], 10))   # 3