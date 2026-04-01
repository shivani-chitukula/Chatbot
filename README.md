# 🤖 Chatbot (LangChain + Groq + Ollama)

A modular AI chatbot built using LangChain with support for Groq (cloud) and Ollama (local) models.
Designed with streaming responses, memory, regeneration, and error handling — focused on real-world usability.

---

## 🚀 Features

* 🔄 **Streaming Responses** (real-time output like ChatGPT)
* 🧠 **Conversation Memory**
* 🔁 **Regenerate Response**
* 🔀 **Model Switching** (Groq / Ollama)
* 🎭 **Role-based Responses** (Teacher, Interviewer, etc.)
* ⚙️ **Adjustable Temperature & Max Tokens**
* 📋 **Clean UI with Streamlit**

---

## 🧱 Tech Stack

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

## ⚙️ Setup Instructions

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

## 🎯 How It Works

* User input → Prompt template → LLM (Groq/Ollama)
* Streaming response displayed in real-time
* Chat history stored using session state
* Regenerate replaces last response instead of duplicating
* Error handling ensures smooth experience

---

## 💡 Highlights

* Built with **modular architecture**
* Handles real-world issues like **token limits and response cutoff**

---


## 🧊 Author

Built as part of a GenAI learning journey with focus on practical system design.
