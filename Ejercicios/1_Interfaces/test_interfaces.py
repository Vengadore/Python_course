import unittest
from elementos_electricos import crear_foco, crear_lampara
from elementos_mecanicos import crear_ventana
from construcciones import crear_casa

class LightTests(unittest.TestCase):

    def _test_crear_casa(self):
        casa = crear_casa()

    def _test_crear_lampara(self):
        lampara = crear_lampara()

    def _test_crear_foco(self):
        foco = crear_foco()

    def _test_encender_foco(self):
        foco = crear_foco()
        self.assertFalse(foco.estado())
        foco.encender()
        self.assertTrue(foco.estado())
        
    def _test_encender_lampara(self):
        lampara = crear_lampara()
        self.assertFalse(lampara.estado())
        lampara.encender()
        self.assertTrue(lampara.estado())

    def _test_conectar_focos(self):
        casa = crear_casa()
        foco0 = crear_foco()
        foco1 = crear_foco()
        foco2 = crear_foco()

        casa.conectar("Foco0",foco0)
        casa.conectar("Foco1",foco1)
        casa.conectar("Foco2",foco2)

        casa.encender("Foco0")
        casa.encender("Foco2")

        self.assertTrue(casa.estado("Foco0"))
        self.assertFalse(casa.estado("Foco1"))
        self.assertTrue(casa.estado("Foco2"))

    def test_conectar_lampara(self):
        casa = crear_casa()

        lampara0 = crear_lampara()

        casa.conectar("Lampara",lampara0)
        self.assertFalse(casa.estado("Lampara"))
        
        casa.encender("Lampara")
        self.assertTrue(casa.estado("Lampara"))


if __name__ == '__main__':
    unittest.main()
