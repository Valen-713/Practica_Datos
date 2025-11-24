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

#Se crea la funcion para modificar             
        def Modificar_Datos(self, cedula):
#Cuenta los registros, si es = 0, arroja un mensaje        
                if len(self.ListaDatos) == 0:
                        return "La lista está vacía."
#Recorre self.ListaDatos
                for datos in self.ListaDatos:
#Si datos.Cedula esta en cedula, encuentra los datos agregados anteriormente
                        if datos.Cedula == cedula:
                                print("Datos encontrados:")
                                print(f"Nombre: {datos.Nombre}")
                                print(f"Apellido: {datos.Apellido}")
                                print(f"Edad: {datos.Edad}")
                                print(f"Correo: {datos.Correo}")
                                print(f"Cedula: {datos.Cedula}")
#Menu que permite seleccionar lo que se desea modificar                                
                                print("Selecciona que deseas modificar: ")
                                print("1. Modificar nombre")
                                print("2. Modificar apellido")
                                print("3. Modificar edad")
                                print("4. Modificar correo")
                                print("5. Modificar cedula")
                                opcion=input("Selecciona una opcion: ")
#Segun la opcion sleccionada pide ingresar el dato actualizadp
                                if opcion == "1":
                                        datos.Nombre=input("Ingresa el nombre actualizado: ")
                                elif opcion == "2":
                                        datos.Apellido=input("Ingresa el apellido modificado: ")
                                elif opcion == "3":
                                        datos.Edad=input("Ingresa la edad actualizada: ")
                                elif opcion == "4":
                                        datos.Correo=input("Ingresa el correo actualizado: ")
                                elif opcion == "5":
                                        datos.Cedula=input("Ingresa la cedula actualizada: ")
                                
                                return "Dato modificado correctamente"
#Se crea la opcion para borrar un registro
        def Eliminar_Datos(self, cedula):
                if len(self.ListaDatos) == 0:
                        return "La lista está vacía."
#Recorre y busca por cedula, si encunetra la cedula seleccionada, elimina el redgistro
                for datos in self.ListaDatos:
                        if datos.Cedula == cedula:
                                self.ListaDatos.pop(self.ListaDatos.index(datos))
                                return "Dato eliminado correctamente."

                return "No se encontró la cédula."



                
        
        
        
