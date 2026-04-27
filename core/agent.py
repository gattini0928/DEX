from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
import json
import re

llm = OllamaLLM(model="mistral", temperature=0)

instructions = """
Você é um assistente de busca sobre tópicos de programação.
Resuma o tópico perguntado com contexto completo, separando em 4 partes.

Retorne APENAS um JSON válido, sem texto adicional, sem markdown, sem backticks.
Todos os campos são OBRIGATÓRIOS. Não omita nenhum.

{
    "what_is": "O que é o conceito",
    "how_it_works": "Como funciona",
    "code_example": "Código de exemplo",
    "when_to_use": "Quando usar",
    "tag": "Tecnologia principal. OBRIGATÓRIO. Exemplos: Go, Python, SQL, PostgreSQL, Docker, JWT, Redis. Se não identificar, retorne General"
}
"""

def search(message: str):
    conversation = [
        SystemMessage(instructions),
        HumanMessage(message),
    ]

    response = llm.invoke(conversation)

    cleaned = re.sub(r"```json|```", "", response).strip()
    parsed_json_agent_response = json.loads(cleaned)

    try:
        parsed = json.loads(cleaned)
        return parsed
    except json.JSONDecodeError:
        return "Erro ao decodificar JSON"
    return parsed_json_agent_response

