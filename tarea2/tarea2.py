def calcular_fila(numero_fila: int) -> list[int]:
    """Calcula la fila 'n' del triángulo de Pascal y devuelve una lista (indexada desde 0)."""
    fila = [1]
    for k in range(1, numero_fila + 1):
        # Fórmula para el elemento k en la fila n del triángulo de Pascal
        valor = fila[k - 1] * (numero_fila + 1 - k) // k
        fila.append(valor)
    return fila


def generar_triangulo_pascal(cantidad_filas: int) -> list[list[int]]:
    """Calcula el triángulo de Pascal con la cantidad de filas especificada y devuelve una lista de filas"""
    return [calcular_fila(fila) for fila in range(cantidad_filas)]


def imprimir_triangulo_pascal(cantidad_filas: int, triangulo: list[list[int]] = None) -> None:
    """Imprime de forma formateada el triángulo de Pascal con la cantidad de líneas especificada.

    - cantidad_filas -- Se trunca a un entero. CUIDADO: Demasiadas filas pueden ser difíciles de visualizar.

    - Opcionalmente, se puede proporcionar un triángulo ya generado para formatearlo e imprimirlo."""

    if cantidad_filas == 0:
        print()
        return

    if triangulo is None:
        triangulo = generar_triangulo_pascal(cantidad_filas)

    ultima_fila = triangulo[-1]

    # Obtener el tamaño del número más grande para calcular el espaciado
    ancho_maximo_numero = len(str(ultima_fila[len(ultima_fila) // 2]))

    # Función interna para formatear una fila del triángulo
    def formatear_fila(fila: list[int]) -> str:
        return " ".join([f"{elemento:^{ancho_maximo_numero}}" for elemento in fila])

    ancho_fila_mas_larga = len(formatear_fila(ultima_fila))

    # Imprimir cada fila formateada y centrada
    for fila in triangulo:
        fila_formateada = formatear_fila(fila)
        # Centrar la fila formateada en el espacio de la fila más larga
        print(f"{fila_formateada:^{ancho_fila_mas_larga}}")


if __name__ == "__main__":
    n_lineas = int(input("Introduce el número de líneas para el triángulo de Pascal: "))

    imprimir_triangulo_pascal(n_lineas)
