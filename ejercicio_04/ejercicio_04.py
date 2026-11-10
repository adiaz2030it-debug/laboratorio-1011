"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] < objetivo:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#
#    1. Caso exito: El elemento en la posición central (`codigos[medio]`) es igual al `objetivo` (se encuentra el código y se devuelve el índice).
#    2. Caso fallo: El índice `izquierda` supera a `derecha` (`izquierda > derecha`), lo que indica que el rango de búsqueda es inválido/vacío (el objetivo no está en la lista y se devuelve -1).
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#
#    Porque la posición `medio` ya ha sido evaluada. Si el elemento no coincidió con el `objetivo`, sabemos con certeza que no está en `medio`. Incluirlo en la siguiente llamada recursiva sería redundante y podría provocar un bucle infinito si el intervalo no reduce su tamaño.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0     |    6    |   3   | 415 > 300 -> Buscar en sublista izquierda: derecha = 2
#       2    |     0     |    2    |   1   | 205 < 300 -> Buscar en sublista derecha: izquierda = 2
#       3    |     2     |    2    |   2   | 310 > 300 -> Buscar en sublista izquierda: derecha = 1
#       4    |     2     |    1    |   —   | izquierda > derecha -> Fin de búsqueda, devuelve -1
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
#
#    En `contar_desde_limite()` el progreso es lineal: en cada paso recursivo el problema se reduce de uno en uno (decrece a ritmo constante $O(n)$). En cambio, `buscar_codigo()` avanza dividiendo por la mitad el espacio de búsqueda en cada llamada recursiva (progreso logarítmico $O(\log n)$), descartando de un solo paso la mitad de los elementos restantes.
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
