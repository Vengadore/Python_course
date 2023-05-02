
class crear_casa:
    def __init__(self) -> None:
        self.objetos = []

    def conectar(self,nombre,nueva_conexion):
        self.objetos.append([nombre,nueva_conexion])
    
    def encender(self,Elemento):
        for nombre,objeto in self.objetos:
            if nombre == Elemento:
                objeto.encender()
    
    def estado(self,Elemento):
        for nombre,objeto in self.objetos:
            if nombre == Elemento:
                return objeto.estado()
    