"""Login corrigido: laboratório local, sem servidor e sem dependências externas."""
import hashlib
import hmac
import secrets
import sqlite3

ITERATIONS = 600_000
LAB_USER = "aluno"
LAB_PASSWORD = "SenhaDeLaboratorio#2026"


def password_hash(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)


def provision_user(connection, username, password):
    salt = secrets.token_bytes(16)
    connection.execute(
        "INSERT INTO users (username, salt, password_hash) VALUES (?, ?, ?)",
        (username, salt, password_hash(password, salt)),
    )
    connection.commit()


def create_lab_db():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL,"
        " salt BLOB NOT NULL, password_hash BLOB NOT NULL)"
    )
    provision_user(connection, LAB_USER, LAB_PASSWORD)
    return connection


def authenticate(connection, username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        return False
    if len(username) > 128 or len(password) > 256:
        return False
    row = connection.execute(
        "SELECT salt, password_hash FROM users WHERE username = ?", (username,)
    ).fetchone()
    salt, expected = row if row else (bytes(16), bytes(32))
    matches = hmac.compare_digest(password_hash(password, salt), expected)
    return row is not None and matches


if __name__ == "__main__":
    db = create_lab_db()
    try:
        print("Login válido:", authenticate(db, LAB_USER, LAB_PASSWORD))
    finally:
        db.close()

