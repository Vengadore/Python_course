from interfaces import energia_electrica

class crear_foco:
    def __init__(self) -> None:
        self.encendido = False

    def encender(self):
        pass
    
    def apagar(self):
        pass

    def estado(self):
        return self.encendido
    

class crear_lampara(energia_electrica):
    def __init__(self) -> None:
        self.estado = False
    
    def encender(self):
        return super().encender()
