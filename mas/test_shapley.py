from shapley import calcular_shapley


agentes = [
    "Analista",
    "Optimizador",
    "Validador"
]


contribuciones = {
    "Analista": 0.30,
    "Optimizador": 0.40,
    "Validador": 0.25
}


resultado = calcular_shapley(
    agentes,
    contribuciones
)


print("Valores de Shapley:")

for agente, valor in resultado.items():
    print(f"{agente}: {valor}")