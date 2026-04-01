from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from .prompt import get_prompt

def get_llm(model_name, temperature,max_tokens):
    if model_name=="Groq":
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=temperature,
            max_tokens=max_tokens
        )
    else:
        return ChatOllama(
            model="llama3",
            temperature=temperature,
            max_tokens=max_tokens
        )


def generate_response_stream(user_input, model_name, temperature, max_tokens, chat_history, role):
    llm=get_llm(model_name, temperature, max_tokens)
    prompt=get_prompt(max_tokens,role)

    chain=prompt | llm

    for chunk in chain.stream({
        "input": user_input,
        "chat_history": chat_history
    }):
        yield chunk.content