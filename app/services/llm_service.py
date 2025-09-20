import ollama
from app.configs.config import settings

def nl_to_sql(question: str, schema: str = "") -> str:
    prompt = f"""
    Convert this into a valid PostgreSQL SQL query.
    Schema: {schema}
    Question: {question}
    Return only SQL.
    """
    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"].strip()
