from crewai import Agent, LLM
from tools import (
    obtener_metricas_dqn,
    evaluar_propuestas_contract_net
)

llm_ollama = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    api_key="ollama"
)

analista_rendimiento = Agent(
    role="Analista de Rendimiento DQN",

    goal=(
        "Analizar las métricas obtenidas por el agente DQN en CartPole "
        "e identificar problemas de estabilidad, convergencia y desempeño."
    ),

    backstory=(
        "Eres un especialista en aprendizaje por refuerzo y evaluación "
        "de modelos DQN. Tu función es interpretar métricas de entrenamiento "
        "y evaluación para detectar oportunidades de mejora."
    ),

    tools=[obtener_metricas_dqn],

    llm=llm_ollama,

    verbose=True
)

optimizador_dqn = Agent(
    role="Especialista en Optimización DQN",

    goal=(
        "Proponer mejoras en los hiperparámetros y estrategia de entrenamiento "
        "del agente DQN utilizando el diagnóstico generado por el analista."
    ),

    backstory=(
        "Eres un especialista en Deep Reinforcement Learning con experiencia "
        "en redes DQN, estrategias epsilon-greedy, replay buffer, actualización "
        "de redes objetivo y ajuste de hiperparámetros."
    ),

    llm=llm_ollama,

    verbose=True
)

validador_estrategias = Agent(
    role="Validador de Estrategias DQN",

    goal=(
        "Evaluar las propuestas de optimización generadas para el agente DQN "
        "y determinar cuál es la más conveniente utilizando un mecanismo "
        "de coordinación Contract Net."
    ),

    backstory=(
        "Eres un especialista en validación experimental y coordinación "
        "de sistemas multiagente. Evalúas estrategias considerando "
        "beneficio, confianza, riesgo y costo."
    ),

    tools=[evaluar_propuestas_contract_net],

    llm=llm_ollama,

    verbose=True
)