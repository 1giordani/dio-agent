"""Exemplo intencionalmente vulnerável. Somente SQLite descartável em memória."""
import sqlite3


def create_lab_db():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    connection.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ("aluno", "SenhaDeLaboratorio#2026"),
    )
    connection.commit()
    return connection


def authenticate(connection, username, password):
    # Falha didática: entrada não confiável altera a estrutura da instrução.
    query = (
        f"SELECT id FROM users WHERE username = '{username}' "
        f"AND password = '{password}'"
    )
    return connection.execute(query).fetchone() is not None

