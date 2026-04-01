from langchain_core.prompts import ChatPromptTemplate

def get_prompt(max_tokens, role):
    safe_target=int(max_tokens * 0.7)

    role_map = {
        "Default": "You are a helpful assistant.",
        "Teacher": "You are a teacher. Explain concepts clearly with examples.",
        "Interviewer": "You are an interviewer. Ask follow-up questions and evaluate answers.",
        "Code Expert": "You are a coding expert. Give precise and technical answers."
    }

    system_text=f"{role_map.get(role)} Answer in about {safe_target} tokens. Keep it complete."

    return ChatPromptTemplate.from_messages([
        ("system", system_text),
        ("placeholder", "{chat_history}"),
        ("user", "{input}")
    ])