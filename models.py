# models.py
from db import get_db_connection

def create_user(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (%s)",
        (name,)
    )

    conn.commit()
    user_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return user_id


def save_message(user_id: int, role: str, content: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (user_id, role, content) VALUES (%s, %s, %s)",
        (user_id, role, content)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_user_messages(user_id: int, limit: int = 5):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT role, content 
        FROM messages 
        WHERE user_id = %s 
        ORDER BY created_at DESC 
        LIMIT %s
        """,
        (user_id, limit)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

