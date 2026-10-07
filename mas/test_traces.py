from trace_collector import registrar_traza, obtener_trazas


registrar_traza(
    agente="Analista de Rendimiento DQN",
    tarea="Analizar métricas",
    exito=True,
    calidad=0.85,
    confianza=0.90
)

registrar_traza(
    agente="Especialista en Optimización DQN",
    tarea="Proponer mejoras",
    exito=True,
    calidad=0.90,
    confianza=0.85
)

registrar_traza(
    agente="Validador de Estrategias DQN",
    tarea="Validar propuestas con Contract Net",
    exito=True,
    calidad=0.88,
    confianza=0.92
)


for traza in obtener_trazas():
    print(traza)