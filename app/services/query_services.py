from app.services.llm_service import nl_to_sql
from app.db.repository import run_query

def ask_database(question: str, schema: str = ""):
    sql = nl_to_sql(question, schema)
    results = run_query(sql)
    return {"question": question, "sql": sql, "results": results}
