from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")
response = llm.invoke("O que é uma goroutine em Go?")

print(response.content)



