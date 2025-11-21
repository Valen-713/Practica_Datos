#Importar las clases a utilizar
from Datos import Datos
from typing import List

#Se cre una clase hija Gestion_Datos donde se crea una lista que va guardar cada persona que sea registrada
class Gestion_Datos:
        def __init__(self):
                self._ListaDatos=[]
                pass
        @property
        def ListaDatos(self)->List:
                return self._ListaDatos
        @ListaDatos.setter
        def ListaDatos(self,ListaDatos:List):
                self._ListaDatos=ListaDatos

#se crea una variable para agregar los datos en la lista 
        def Agregar_Datos(self,datos:Datos)->Datos:
                self.ListaDatos.append(datos)

#Se crea una variable la cual ayudara a consultar a la persona por su numero de cedula
        def Consultar_Datos(self, Cedula):
                for datos in self.ListaDatos:
                        if datos.Cedula == Cedula:
                                return datos
                        
        def Modificar_Datos(self, cedula):
                if len(self.listaDatos) == 0:
                        return "La lista está vacía."
                for datos in self.listaDatos:
                        if datos.cedula == cedula:
                                print("Datos encontrados:")
                                print(f"Nombre: {datos.nombre}")
                                print(f"Apellido: {datos.apellido}")
                                print(f"Edad: {datos.edad}")
                                print(f"Correo: {datos.correo}")
                                print(f"Cédula: {datos.cedula}")
                
        
        
        
