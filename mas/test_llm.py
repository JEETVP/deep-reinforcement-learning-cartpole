from crewai import LLM

llm_ollama = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    api_key="ollama"
)

respuesta = llm_ollama.call(
    "Responde únicamente con estas dos palabras: conexión correcta"
)

print(respuesta)