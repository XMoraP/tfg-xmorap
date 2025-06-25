# Este es un segmentador que parte el texto en aproximadamente 512 carácteres. 

from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils import embedding_functions
from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

login(token=hf_token)  

with open("./el_quijote.txt", "r", encoding="utf-8") as file:
    quijote_txt = file.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False
)

chunks = text_splitter.split_text(quijote_txt)  

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(path="./database")
collection = client.create_collection(
    name="quijoteDBTextStructure",
    embedding_function=sentence_transformer_ef
)

collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]  
)

print(f"Se cargaron {len(chunks)} chunks del Quijote en ChromaDB.")
