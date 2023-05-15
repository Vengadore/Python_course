import unittest
from complejos.estructura import crear_complejo


class creacion_elementos(unittest.TestCase):

    def test_crear_numero_complejo(self):
        Complejo_ejemplo = crear_complejo(1,1)
        self.assertIsNotNone(Complejo_ejemplo)

    def test_real_0(self):
        Complejo_ejemplo = crear_complejo(0,1)
        self.assertIsNotNone(Complejo_ejemplo)

    def test_complejo_0(self):
        Complejo_ejemplo = crear_complejo(1,0)
        self.assertIsNotNone(Complejo_ejemplo)

if __name__ == "__main__":
    unittest.main()