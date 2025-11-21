#Importar las clases a utilizar
from typing import List

#Se crea la clase Datos con setter y getter para poder insertar los datos requeridos

class Datos:
    def __init__ (self):
        pass
    
    @property
    def Nombre(self)->str:
        return self._nombre

    @Nombre.setter
    def Nombre (self,Nombre: str):
        self._nombre = Nombre
    
    @property
    def Apellido(self)-> str:
        return self._apellido
    
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self._apellido =Apellido
    
    @property
    def Edad(self)-> int:
        return self._edad 
    @Edad.setter
    def Edad(self, Edad: int):
        self._edad = Edad
        
    @property
    def Cedula(self)-> int:
        return self._cedula
    @Cedula.setter
    def Cedula(self, Cedula: int):
        self._cedula = Cedula
    
    @property
    def Correo(self)-> str:
        return self._correo
    
    @Correo.setter
    def Correo(self, Correo: str):
        self._correo = Correo