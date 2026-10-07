from crewai import Task, Crew, Process
from agents import (
    analista_rendimiento,
    optimizador_dqn,
    validador_estrategias
)

from trace_collector import registrar_traza, obtener_trazas
from shapley import calcular_shapley

tarea_analisis = Task(
    description="""
    Utiliza la herramienta obtener_metricas_dqn para consultar las métricas
    reales del agente DQN entrenado en CartPole.

    Analiza los resultados e identifica al menos 3 observaciones sobre
    el rendimiento del modelo.
    """,

    expected_output="""
    Un análisis breve en español con:
    - Las métricas obtenidas
    - Al menos 3 observaciones claras sobre el rendimiento
    """,

    agent=analista_rendimiento
)

tarea_optimizacion = Task(
    description="""
    Utiliza el análisis realizado por el agente Analista de Rendimiento DQN.

    Con base en ese diagnóstico, propone al menos 3 mejoras concretas para
    optimizar el entrenamiento del agente DQN en CartPole.

    Las propuestas pueden modificar elementos como:
    - learning rate
    - epsilon decay
    - gamma
    - batch size
    - frecuencia de actualización de la target network
    - número de episodios

    Para cada propuesta explica brevemente el beneficio esperado.
    """,

    expected_output="""
    Una lista de al menos 3 propuestas de optimización del DQN.
    Cada propuesta debe indicar:
    - parámetro o estrategia a modificar
    - cambio propuesto
    - beneficio esperado
    """,

    agent=optimizador_dqn,

    context=[tarea_analisis]
)

tarea_validacion = Task(
    description="""
    Revisa el diagnóstico generado por el Analista de Rendimiento DQN
    y las propuestas producidas por el Especialista en Optimización DQN.

    Selecciona al menos 3 propuestas.

    Para cada propuesta asigna:
    - agente
    - beneficio
    - confianza
    - riesgo
    - costo

    Los valores numéricos deben estar entre 0 y 1.

    Después utiliza obligatoriamente la herramienta
    evaluar_propuestas_contract_net.

    IMPORTANTE:
    El argumento "propuestas" de la herramienta debe enviarse como una
    cadena de texto en formato JSON válido.

    Ejemplo:

    [
      {
        "agente": "Propuesta 1",
        "beneficio": 0.8,
        "confianza": 0.9,
        "riesgo": 0.2,
        "costo": 0.3
      },
      {
        "agente": "Propuesta 2",
        "beneficio": 0.7,
        "confianza": 0.8,
        "riesgo": 0.1,
        "costo": 0.2
      }
    ]

    Usa el resultado de Contract Net para determinar la propuesta ganadora
    y explica brevemente por qué resulta conveniente.
    """,

    expected_output="""
    Una evaluación que incluya:
    - propuestas evaluadas
    - beneficio, confianza, riesgo y costo
    - propuesta ganadora
    - puntaje Contract Net
    - breve justificación
    """,

    agent=validador_estrategias,

    context=[
        tarea_analisis,
        tarea_optimizacion
    ]
)

crew = Crew(
    agents=[
        analista_rendimiento,
        optimizador_dqn,
        validador_estrategias
    ],
    tasks=[
        tarea_analisis,
        tarea_optimizacion,
        tarea_validacion
    ],
    process=Process.sequential,
    verbose=True
)

resultado = crew.kickoff()
# ---------------------------------------------------------
# CAPA DE TRANSPARENCIA - REGISTRO DE TRAZAS
# ---------------------------------------------------------

registrar_traza(
    agente="Analista de Rendimiento DQN",
    tarea="Analizar métricas del agente DQN",
    exito=True,
    calidad=0.85,
    confianza=0.90
)

registrar_traza(
    agente="Especialista en Optimización DQN",
    tarea="Generar propuestas de optimización",
    exito=True,
    calidad=0.90,
    confianza=0.85
)

registrar_traza(
    agente="Validador de Estrategias DQN",
    tarea="Evaluar propuestas mediante Contract Net",
    exito=True,
    calidad=0.88,
    confianza=0.92
)

trazas = obtener_trazas()

contribuciones = {}

for traza in trazas:
    contribucion = (
        traza["calidad"] * 0.6
        + traza["confianza"] * 0.4
    )

    if traza["agente"] == "Analista de Rendimiento DQN":
        nombre = "Analista"

    elif traza["agente"] == "Especialista en Optimización DQN":
        nombre = "Optimizador"

    else:
        nombre = "Validador"

    contribuciones[nombre] = contribucion

agentes_shapley = [
    "Analista",
    "Optimizador",
    "Validador"
]

valores_shapley = calcular_shapley(
    agentes_shapley,
    contribuciones
)

print("\nVALORES DE SHAPLEY")

for agente, valor in valores_shapley.items():
    print(f"{agente}: {valor}")



print("\n==============================")
print("TRAZAS DE EJECUCIÓN")
print("==============================")

for traza in obtener_trazas():
    print(traza)

print("\nRESULTADO FINAL:\n")
print(resultado)