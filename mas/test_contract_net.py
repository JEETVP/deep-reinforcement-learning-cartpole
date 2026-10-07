from coordination import contract_net

propuestas = [
    {
        "agente": "propuesta_1",
        "beneficio": 0.85,
        "confianza": 0.90,
        "riesgo": 0.20,
        "costo": 0.30
    },
    {
        "agente": "propuesta_2",
        "beneficio": 0.75,
        "confianza": 0.80,
        "riesgo": 0.10,
        "costo": 0.20
    },
    {
        "agente": "propuesta_3",
        "beneficio": 0.95,
        "confianza": 0.70,
        "riesgo": 0.40,
        "costo": 0.35
    }
]

resultado = contract_net(propuestas)

print(resultado)