class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara 
    def llamar(self):
        print(f"Estas llamando desde tu: {self.modelo}")
    def colgar(self):
        print(f"costaste la llamada desde tu: {self.modelo}")    
    # marca="sansung" #propiedades fijas, se pueden cambiar fuera de la clase.
    # modelo="s23"
    # camara="48mp"
cel=Celular("sansun","s23","48mp")
cel2=Celular("aple","iphon 15","96mp")
cel2.llamar()