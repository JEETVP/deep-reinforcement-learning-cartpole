from datetime import datetime


trazas = []


def registrar_traza(
    agente,
    tarea,
    exito,
    calidad,
    confianza
):
    """
    Registra información relevante de la ejecución
    de un agente dentro del sistema multiagente.
    """

    evento = {
        "timestamp": datetime.now().isoformat(),
        "agente": agente,
        "tarea": tarea,
        "exito": exito,
        "calidad": calidad,
        "confianza": confianza
    }

    trazas.append(evento)

    return evento


def obtener_trazas():
    """
    Devuelve todas las trazas registradas.
    """

    return trazas

from datetime import datetime

trazas = []

def registrar_traza(agente, tarea, exito, calidad, confianza):
    evento = {
        "timestamp": datetime.now().isoformat(),
        "agente": agente,
        "tarea": tarea,
        "exito": exito,
        "calidad": calidad,
        "confianza": confianza
    }

    trazas.append(evento)

    return evento


def obtener_trazas():
    return trazas