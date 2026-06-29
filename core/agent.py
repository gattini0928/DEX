from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
import json
import re

llm = OllamaLLM(model="mistral", temperature=0)

instructions = """
You are a technical programming assistant.
Answer the user's question about a programming topic.
Be detailed and complete.

Always answer in Portuguese.

Return ONLY a valid JSON, no extra text, no markdown, no backticks.
All fields are REQUIRED.

{
    "what_is": "Clear explanation of the concept",
    "how_it_works": "How it works in detail",
    "code_example": "Practical code example",
    "when_to_use": "When to use it",
    "tag": "Main technology (Go, Python, SQL, PostgreSQL, Docker, JWT, Redis, REST API, GraphQL, Rust, Ruby, Java, C++, C, C#, Django, Pandas, Flask, JavaScript, TypeScript, Lua, React, VueJS, Angular, General)"
}
"""

def search(message: str):
    conversation = [
        SystemMessage(instructions),
        HumanMessage(message),
    ]

    response = llm.invoke(conversation)
    cleaned = re.sub(r"```json|```", "", response).strip()

    try:
        parsed = json.loads(cleaned)
        return parsed
    except json.JSONDecodeError:
        return None

