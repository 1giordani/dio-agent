import unittest
import app
from examples import app_vulneravel


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.db = app.create_lab_db()

    def tearDown(self):
        self.db.close()

    def test_baseline_demonstra_falha(self):
        db = app_vulneravel.create_lab_db()
        try:
            self.assertTrue(app_vulneravel.authenticate(db, "aluno' --", "errada"))
        finally:
            db.close()

    def test_login_valido(self):
        self.assertTrue(app.authenticate(self.db, app.LAB_USER, app.LAB_PASSWORD))

    def test_senha_incorreta(self):
        self.assertFalse(app.authenticate(self.db, app.LAB_USER, "errada"))

    def test_usuario_inexistente(self):
        self.assertFalse(app.authenticate(self.db, "desconhecido", "errada"))

    def test_injecao_no_usuario_bloqueada(self):
        self.assertFalse(app.authenticate(self.db, "aluno' --", "errada"))

    def test_injecao_na_senha_bloqueada(self):
        self.assertFalse(app.authenticate(self.db, app.LAB_USER, "' OR '1'='1"))

    def test_aspas_em_nome_legitimo(self):
        app.provision_user(self.db, "O'Connor", "senha de exemplo")
        self.assertTrue(app.authenticate(self.db, "O'Connor", "senha de exemplo"))

    def test_senha_nao_e_persistida_em_texto(self):
        row = self.db.execute("SELECT salt, password_hash FROM users").fetchone()
        self.assertEqual(len(row[0]), 16)
        self.assertEqual(len(row[1]), 32)
        self.assertNotEqual(row[1], app.LAB_PASSWORD.encode())

    def test_salts_distintos(self):
        app.provision_user(self.db, "outra", app.LAB_PASSWORD)
        rows = self.db.execute("SELECT salt, password_hash FROM users").fetchall()
        self.assertNotEqual(rows[0][0], rows[1][0])
        self.assertNotEqual(rows[0][1], rows[1][1])

    def test_integridade_apos_entrada_maliciosa(self):
        self.assertFalse(app.authenticate(self.db, "'; DROP TABLE users; --", "x"))
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 1)

    def test_tipo_e_tamanho_invalidos(self):
        self.assertFalse(app.authenticate(self.db, None, "x"))
        self.assertFalse(app.authenticate(self.db, "a" * 129, "x"))
        self.assertFalse(app.authenticate(self.db, "aluno", "x" * 257))


if __name__ == "__main__":
    unittest.main()

