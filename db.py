import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        resume_text TEXT,
        feedback TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_resume(name, resume_text, feedback):
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO resumes (name, resume_text, feedback) VALUES (?, ?, ?)",
        (name, resume_text, feedback)
    )
    conn.commit()
    conn.close()

def fetch_resumes():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, feedback FROM resumes")
    rows = cursor.fetchall()
    conn.close()
    return rows
