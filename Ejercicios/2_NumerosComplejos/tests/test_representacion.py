import unittest
from complejos.estructura import crear_complejo
from complejos.representacion import rectangular,polar


class creacion_elementos(unittest.TestCase):

    def test_representacion_rectangular(self):
        Complejo_ejemplo = crear_complejo(1,1)
        Complejo_rectangular = rectangular(Complejo_ejemplo)

        self.assertEqual(Complejo_rectangular,"1 + 1j","La representacion rectangular no es correcta")

    def test_representacion_polar(self):
        Complejo_ejemplo = crear_complejo(1,1)
        Complejo_polar = polar(Complejo_ejemplo)

        self.assertEqual(Complejo_polar.split(" ")[0],"1.414","El modulo de la representación polar no es correcta")
        self.assertEqual(Complejo_polar.split(" ")[1],"45.0°","El angulo de la representación polar no es correcta")




if __name__ == "__main__":
    unittest.main()