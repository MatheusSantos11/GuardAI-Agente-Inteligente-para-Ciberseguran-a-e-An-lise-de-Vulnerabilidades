"""Consulta parametrizada para o laboratório. Em produção, use hash de senha."""
import sqlite3


def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    query = "SELECT id FROM users WHERE username = ? AND password = ?"
    return conn.execute(query, (username, password)).fetchone() is not None
