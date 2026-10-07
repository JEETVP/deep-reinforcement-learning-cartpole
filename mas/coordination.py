def contract_net(propuestas):
    """
    Evalúa distintas propuestas y selecciona la mejor
    considerando beneficio, confianza, riesgo y costo.
    """

    mejor_propuesta = None
    mejor_puntaje = float("-inf")

    for propuesta in propuestas:
        beneficio = propuesta["beneficio"]
        confianza = propuesta["confianza"]
        riesgo = propuesta["riesgo"]
        costo = propuesta["costo"]

        puntaje = (
            beneficio * 0.40
            + confianza * 0.30
            - riesgo * 0.20
            - costo * 0.10
        )

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_propuesta = propuesta

    return {
        "ganador": mejor_propuesta,
        "puntaje": round(mejor_puntaje, 3)
    }