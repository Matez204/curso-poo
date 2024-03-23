class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hablando...")

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        return f"me llamo {self.nombre} y {self.mostrar_habilidad()}"
        
cosa=EmpleadoArtista("Roberto", 22,"colombiano","cocinar",2000,"Columbia")

print(issubclass(EmpleadoArtista,Artista))#Nos dice si es una subclase de alguien
print(isinstance(cosa, Artista))#Nos dice si es un obojeto de esa clase 
# print(cosa.presentarse())