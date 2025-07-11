import os
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# 1. Set Gemini API key
os.environ["GOOGLE_API_KEY"] = "#"  # Replace with your actual key

# 2. Load saved FAISS vector index (must match embedding model used in Colab)
embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.load_local(
    "faiss_index", 
    embeddings, 
    allow_dangerous_deserialization=True
)

# 3. Load Gemini 1.5 Flash as LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0.5
)

# 4. Create QA chain using LangChain's RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)
