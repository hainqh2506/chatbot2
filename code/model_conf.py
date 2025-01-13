import tiktoken
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from transformers import AutoTokenizer
from langchain_together import ChatTogether , Together
import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from pyvi.ViTokenizer import tokenize
from typing import List, Optional
from langchain_core.embeddings import Embeddings
import numpy as np
# Thay các dòng load_dotenv() và os.getenv() bằng st.secrets
import streamlit as st
# dùng cho secrets.toml
def load_gpt4o_mini_model(model_name: str = "gpt-4o-mini", max_tokens: int = 512):
    return ChatOpenAI(api_key=st.secrets["api"]["openai"], model=model_name, max_tokens=max_tokens)

def load_gemini15(model_name: str = "gemini-1.5-flash"):
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.7,
        api_key=st.secrets["api"]["gemini1"]
    )

def load_groq_model(chat_model_name: str = "llama-3.3-70b-versatile"):
    return ChatGroq(api_key=st.secrets["api"]["groq"], model_name=chat_model_name)

def load_together_model(model_name: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo"):
    return ChatTogether(api_key=st.secrets["api"]["together"], model_name=model_name)