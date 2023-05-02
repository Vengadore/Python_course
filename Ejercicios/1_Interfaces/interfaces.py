from abc import ABC, abstractmethod


class energia_electrica(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.estado = False
        pass
    
    @abstractmethod
    def encender(self):
        """Al llamar a este método el objeto debe encenderse
        """
        pass
    
    @abstractmethod
    def apagar(self):
        """Al llamar a este método el objeto debe apagarse
        """
        pass

    @abstractmethod
    def estado(self):
        """Este método indica si el objeto está energizado
        """
        pass