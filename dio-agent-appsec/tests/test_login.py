import sqlite3
import unittest
from examples.app_fixed import login


class TestLoginSeguro(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
        self.conn.execute('INSERT INTO users(username,password) VALUES (?, ?)', ('aluna', 'senha-de-laboratorio'))

    def tearDown(self):
        self.conn.close()

    def test_credenciais_validas(self):
        self.assertTrue(login(self.conn, 'aluna', 'senha-de-laboratorio'))

    def test_credenciais_invalidas(self):
        self.assertFalse(login(self.conn, 'aluna', 'incorreta'))

    def test_entrada_com_aspas_e_tratada_como_dado(self):
        self.assertFalse(login(self.conn, "aluna'", 'senha-de-laboratorio'))

    def test_tabela_permanece_disponivel(self):
        login(self.conn, "texto' ;", 'errada')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM users').fetchone()[0], 1)


if __name__ == '__main__':
    unittest.main()
