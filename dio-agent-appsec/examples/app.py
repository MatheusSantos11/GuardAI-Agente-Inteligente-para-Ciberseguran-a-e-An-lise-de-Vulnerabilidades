"""Exemplo intencionalmente inseguro. Apenas demonstração local e estática."""
import sqlite3


def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    # VULNERÁVEL: concatena dados externos no texto da consulta.
    query = "SELECT id FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return conn.execute(query).fetchone() is not None
