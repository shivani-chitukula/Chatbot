# 🤖 Chatbot (LangChain + Groq + Ollama)

A modular AI chatbot built using LangChain, with support for both Groq (cloud-based models) and Ollama (local models).

The application focuses on real-world usability, featuring streaming responses, conversation memory, response regeneration.


---

## Features

* **Streaming Responses** (real-time output like ChatGPT)
* **Conversation Memory**
* **Regenerate Response**
* **Model Switching** (Groq / Ollama)
* **Role-based Responses** (Teacher, Interviewer, etc.)
* **Adjustable Temperature & Max Tokens**
* **Clean UI with Streamlit**

---

## Tech Stack

* Python
* LangChain
* Streamlit
* Groq API
* Ollama (local LLMs)
---

## 📁 Project Structure

```
Chatbot/
│── app.py
│── utils/
│     ├── llm.py
│     ├── prompt.py
│     ├── memory.py
│── .env
│── requirements.txt
│── .gitignore
```

---

## Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

---

### 2️⃣ Create environment

```
conda create -n genai python=3.10
conda activate genai
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=chatbot-project
```

---

### 5️⃣ (Optional) Setup Ollama

Install Ollama and pull a model:

```
ollama pull llama3
```

---

### 6️⃣ Run the app

```
python -m streamlit run app.py
```

---

## How It Works

* User input → Prompt template → LLM (Groq/Ollama)
* Streaming response displayed in real-time
* Chat history stored using session state
* Regenerate replaces last response instead of duplicating
* Error handling ensures smooth experience

---
## UI Preview

<img width="1600" height="757" alt="image" src="https://github.com/user-attachments/assets/37e284f4-3119-46d7-a8b8-c6c1877f9202" />


## 📊 LangSmith Tracing

<img width="1600" height="808" alt="image" src="https://github.com/user-attachments/assets/3ffe8c30-5198-4c92-968c-2bdee12e943d" />

## 💡 Highlights

* Built with **modular architecture**
* Handles real-world issues like **token limits and response cutoff**

---

