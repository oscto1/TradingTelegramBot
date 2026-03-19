from database.db import get_connection

def create_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,)
    )

    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))

    user = cursor.fetchone()

    conn.close()
    return user

def set_region(user_id, region):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET region = ? WHERE user_id = ?", (region, user_id))

    conn.commit()
    conn.close()

def ensure_user(user_id):
    user = get_user(user_id)

    if not user:
        create_user(user_id)
        return False  # newly created

    return True  # already existed