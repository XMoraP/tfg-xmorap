import os
import chromadb
from chromadb.utils import embedding_functions

# Usa la ruta absoluta al directorio "database" junto al archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(BASE_DIR, "database")

_EMB_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def _query_collection(name: str, query: str, n_results: int = 3):
    client = chromadb.PersistentClient(path=_DB_PATH)
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=_EMB_MODEL
    )
    collection = client.get_collection(
        name=name,
        embedding_function=embedding_fn
    )
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results

def get_context_ts(query: str):
    return _query_collection(name="quijoteDBTextStructure", query=query)

def get_context_lt(query: str):
    return _query_collection(name="quijoteBDLongToken", query=query)

def get_context_lc(query: str):
    return _query_collection(name="quijoteBDLongChar", query=query)
