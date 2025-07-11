echo "# 🏏 Cricket Chatbot using LangChain + Gemini + Flask

This is a smart chatbot that answers all your cricket-related questions using **LangChain** for retrieval, **FAISS** for vector storage, and **Google Gemini API** as the language model. It is built in **Google Colab** and deployed using **Flask**.

## 🚀 Features

- 💬 Ask natural language questions about cricket (rules, players, stats, etc.)
- 📚 Uses a custom \`cricket_knowledge.txt\` file as a knowledge base
- 🧠 Powered by LangChain RAG (Retrieval-Augmented Generation)
- 🔍 Retrieves relevant info using FAISS vector store
- 🌐 Gemini model (via Google Generative AI) for smart responses
- 🧪 Built in Google Colab, deployed with Flask UI

## 📁 Project Structure

\`\`\`
cricket_chatbot/
├── app.py
├── rag_setup.py
├── cricket_knowledge.txt
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
├── requirements.txt
└── README.md
\`\`\`

## 🛠️ Setup Instructions

### 🔹 1. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 🔹 2. Run the Flask app

\`\`\`bash
python app.py
\`\`\`

Then open: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🔑 Gemini API Key

Set your key like this:

\`\`\`python
import os
os.environ[\"GEMINI_API_KEY\"] = \"your-api-key-here\"
\`\`\`

[→ Get Gemini API Key](https://makersuite.google.com/app)

## 🧠 How It Works (LangChain RAG)

- Loads \`cricket_knowledge.txt\` using LangChain DocumentLoader
- Splits and embeds using HuggingFaceEmbeddings + FAISS
- Uses LangChain's \`RetrievalQA\` chain to connect vector DB and Gemini
- Gemini model generates the final answer based on retrieved context

