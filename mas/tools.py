import json
from crewai.tools import tool
from coordination import contract_net


@tool("obtener_metricas_dqn")
def obtener_metricas_dqn(env: str = "CartPole-v1"):
    """
    Devuelve las métricas base del agente DQN entrenado en CartPole.

    Args:
        env: Nombre del entorno de Gymnasium.
    """

    metricas = {
        "entorno": env,
        "reward_promedio": 125.5,
        "reward_maximo": 132,
        "reward_minimo": 116
    }

    return str(metricas)

@tool("evaluar_propuestas_contract_net")
def evaluar_propuestas_contract_net(propuestas: str):
    """
    Evalúa propuestas de optimización del agente DQN mediante
    un mecanismo Contract Net.

    El parámetro propuestas debe ser una cadena JSON que contenga
    una lista de propuestas.

    Cada propuesta debe incluir:
    - agente
    - beneficio
    - confianza
    - riesgo
    - costo

    Los valores beneficio, confianza, riesgo y costo deben estar
    entre 0 y 1.
    """

    try:
        propuestas_lista = json.loads(propuestas)

        if not isinstance(propuestas_lista, list):
            return "Error: propuestas debe contener una lista JSON."

        resultado = contract_net(propuestas_lista)

        return str(resultado)

    except json.JSONDecodeError as error:
        return f"Error al interpretar las propuestas: {error}"