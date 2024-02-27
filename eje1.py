class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    def estudiar(self):
        print("Estudiando... ")
nombre=input("Digame su nombre ")
edad=int(input("Digame su edad "))
grado=int(input("Digame su grado "))

estudiante=Estudiante(nombre,edad,grado)
print(f"""
Datos del estudiante:\n
Nombre: {estudiante.nombre} 
Edad: {estudiante.edad} 
Grado: {estudiante.grado} 
      """)

estudiar =input()
if estudiar.lower() == "estudiar":
    estudiante.estudiar()