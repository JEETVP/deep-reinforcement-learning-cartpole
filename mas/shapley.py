from itertools import combinations
from math import factorial

def valor_coalicion(coalicion, contribuciones):
    if len(coalicion) == 0:
        return 0.0

    utilidad = 0.0

    for agente in coalicion:
        utilidad += contribuciones[agente]

    if len(coalicion) > 1:
        utilidad += 0.05 * (len(coalicion) - 1)

    return min(utilidad, 1.0)


def calcular_shapley(agentes, contribuciones):
    n = len(agentes)
    shapley = {}

    for agente in agentes:
        valor = 0.0

        otros = [
            a for a in agentes
            if a != agente
        ]

        for tamano in range(len(otros) + 1):
            for subconjunto in combinations(otros, tamano):

                coalicion = list(subconjunto)

                valor_sin = valor_coalicion(
                    coalicion,
                    contribuciones
                )

                valor_con = valor_coalicion(
                    coalicion + [agente],
                    contribuciones
                )

                contribucion_marginal = valor_con - valor_sin

                peso = (
                    factorial(len(coalicion))
                    * factorial(n - len(coalicion) - 1)
                    / factorial(n)
                )

                valor += peso * contribucion_marginal

        shapley[agente] = round(valor, 4)

    return shapley