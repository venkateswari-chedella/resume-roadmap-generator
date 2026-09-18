import sqlite3
import os

DB_PATH = "database/users.db"


def create_database():
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            education TEXT,
            skills TEXT,
            projects TEXT,
            experience TEXT,
            career_goal TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_user(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users
        (name, email, phone, education, skills, projects, experience, career_goal)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data["phone"],
        data["education"],
        data["skills"],
        data["projects"],
        data["experience"],
        data["career_goal"]
    ))

    conn.commit()
    conn.close()
