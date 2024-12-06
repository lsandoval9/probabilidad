import random
from itertools import product
from decimal import Decimal, getcontext

# Configurar la precisión de los decimales (por ejemplo, 20 dígitos)
getcontext().prec = 20


def lanzar_dados(n_dados):
    """Simula el lanzamiento de N dados de 6 caras.

    Args:
      n_dados: El número de dados a lanzar.

    Returns:
      Una tupla con los resultados de cada dado.
    """
    resultados = []
    for _ in range(n_dados):
        resultados.append(random.randint(1, 6))
    return tuple(resultados)


def generar_espacio_muestral(n_dados):
    """Genera el espacio muestral para N dados de 6 caras.

    Args:
      n_dados: El número de dados.

    Returns:
      Una lista de tuplas, donde cada tupla representa un resultado posible.
    """
    return list(product(range(1, 7), repeat=n_dados))


def calcular_probabilidades(espacio_muestral):
    """Calcula las probabilidades de cada resultado en el espacio muestral.

    Args:
      espacio_muestral: Una lista de tuplas con todos los resultados posibles.

    Returns:
      Un diccionario donde las claves son los resultados y los valores son sus probabilidades.
    """
    total_resultados = Decimal(len(espacio_muestral))
    probabilidades = {}
    for resultado in espacio_muestral:
        if resultado in probabilidades:
            probabilidades[resultado] += Decimal(1) / total_resultados
        else:
            probabilidades[resultado] = Decimal(1) / total_resultados
    return probabilidades


if __name__ == "__main__":
    # Solicitar al usuario el número de dados
    n_dados = int(input("Introduce el número de dados a lanzar: "))

    # Simular el lanzamiento de dados
    resultados_lanzamiento = lanzar_dados(n_dados)
    print("Resultados del lanzamiento:", resultados_lanzamiento)

    # Generar el espacio muestral
    espacio_muestral = generar_espacio_muestral(n_dados)
    print("\nEspacio muestral:")
    for i, resultado in enumerate(espacio_muestral):
        print(resultado, end=" ")
        if (i + 1) % 6 == 0:
            print()

    # Calcular las probabilidades
    probabilidades = calcular_probabilidades(espacio_muestral)

    # Imprimir las probabilidades
    print("\n\nProbabilidades:")
    for resultado, probabilidad in probabilidades.items():
        print(f"Resultado: {resultado}, Probabilidad: {probabilidad}")
