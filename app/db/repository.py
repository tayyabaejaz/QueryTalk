from app.db.connection import get_connection

def run_query(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        return results
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
