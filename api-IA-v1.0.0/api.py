import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from contexts import get_context_ts, get_context_lt, get_context_lc
import ollama

app = FastAPI()

conversations_prompt_rag = {}
conversations_prompt = {}
conversations_finetuning = {}


class QuestionRequest(BaseModel):
    question: str

@app.post("/llama_prompt_rag")
async def get_answer(request: QuestionRequest, req: Request):
    question = request.question
    user_ip = req.client.host

    ctx_ts = get_context_ts(question)
    ctx_lt = get_context_lt(question)
    ctx_lc = get_context_lc(question)

    docs_ts = ctx_ts.get("documents", [[]])[0]
    context_str_ts = "\n".join(f"Documento {i+1}:\n{doc}" for i, doc in enumerate(docs_ts))

    if user_ip not in conversations_prompt_rag:
        conversations_prompt_rag[user_ip] = []

    historial = "\n".join(
        f"Usuario: {q}\nDon Quijote: {r}" for q, r in conversations_prompt_rag[user_ip]
    )

    prompt = f"""
                Instructions:
                - Use these fragments to answer. Do not invent facts beyond them.
                - Your response must sound as if you personally lived these events.
                - Respond in old Spanish, with solemnity, and never break character.
                - Do not quote the text directly, but use its ideas as memories.
                - Do not exceed 7 lines.

                Fragments from your adventures:
                {context_str_ts}

                Previous conversation:
                {historial}

                Question: {question}
            """

    messages = [
        {"role": "system", "content": "You are Don Quixote of La Mancha and you always respond in old Spanish."},
        {"role": "user", "content": prompt}
    ]

    print("🔹 Mensaje enviado al modelo:")
    for m in messages:
        print(f"{m['role']}: {m['content']}\n")

    response = ollama.chat(
        model='llama3.2',
        messages=messages,
    )

    answer = response['message']
    conversations_prompt_rag[user_ip].append((question, answer))

    if len(conversations_prompt_rag[user_ip]) >= 3:
        conversations_prompt_rag[user_ip] = []

    return {"respuesta": answer}

@app.post("/llama_finetuning")
async def get_answer(request: QuestionRequest, req: Request):
    question = request.question
    user_ip = req.client.host

    if user_ip not in conversations_finetuning:
        conversations_finetuning[user_ip] = []

    historial = "\n".join(
        f"Usuario: {q}\nDon Quijote: {r}" for q, r in conversations_finetuning[user_ip]
    )

    prompt = f"""
                {historial}

                Question: {question}
            """

    messages = [
        {"role": "system", "content": "You are Don Quixote of La Mancha and you always respond in old Spanish."},
        {"role": "user", "content": prompt}
    ]

    print("Mensaje enviado al modelo:")
    for m in messages:
        print(f"{m['role']}: {m['content']}\n")

    response = ollama.chat(
        model='don_quijote_v6',
        messages=messages,
    )

    answer = response['message']
    conversations_finetuning[user_ip].append((question, answer))

    if len(conversations_finetuning[user_ip]) >= 5:
        conversations_finetuning[user_ip] = []

    return {"respuesta": answer}

@app.post("/llama_prompt")
async def get_answer(request: QuestionRequest, req: Request):
    question = request.question
    user_ip = req.client.host

    if user_ip not in conversations_prompt:
        conversations_prompt[user_ip] = []

    historial = "\n".join(
        f"Usuario: {q}\nDon Quijote: {r}" for q, r in conversations_prompt[user_ip]
    )

    prompt = f"""
                Instructions:
                - Your response must sound as if you personally lived these events.
                - Respond in old Spanish, with solemnity, and never break character.
                - Do not exceed 7 lines.

                Previous conversation:
                {historial}

                Question: {question}
            """

    messages = [
        {"role": "system", "content": "You are Don Quixote of La Mancha and you always respond in old Spanish."},
        {"role": "user", "content": prompt}
    ]

    print("Mensaje enviado al modelo:")
    for m in messages:
        print(f"{m['role']}: {m['content']}\n")

    response = ollama.chat(
        model='llama3.2',
        messages=messages,
    )

    answer = response['message']
    conversations_prompt[user_ip].append((question, answer))

    if len(conversations_prompt[user_ip]) >= 5:
       conversations_prompt[user_ip] = []

    return {"respuesta": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
