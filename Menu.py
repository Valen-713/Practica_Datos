#Importar las clases a utilizar
from Datos import Datos
from Gestion_Datos import Gestion_Datos
#Instancias funciones
GD = Gestion_Datos()
Agregar = Datos()
Eliminar = Datos()

#Creacion de menu a utilizar
while True:
    print("1.Agregar")
    print("2.Consultar")
    print("3.Modificar")
    print("4.Eliminar")
    print("5.Salir")   
    opcion = input("Selecciona una opcion: ")

#Se crea la opcion 1 donde se puede digitar los datos de cada persona
    if opcion == "1":
        Agregar.Nombre =str(input("Digite el nombre: "))
        Agregar.Apellido =str(input("Digite el apellido: "))
        Agregar.Edad =int(input("Digite la edad: "))
        Agregar.Cedula =int(input("Digite el numero de cedula: "))
        Agregar.Correo =input("Ingrese el correo: ")     
        GD.Agregar_Datos(Agregar)
        print("Datos agregados correctamente.\n")

#Se crea la opcion 2 donde se digita el numero de cedula para hallar a esa persona con sus datos correspondientes
    elif opcion == '2':
        cedula = int(input("Ingrese la cedula a consultar: "))
        resultado = GD.Consultar_Datos(cedula)
        

#Se imprime los resultados
        if resultado:
            print("---- Datos encontrados ----")
            print(f"Nombre: {resultado.Nombre}")
            print(f"Apellido: {resultado.Apellido}")
            print(f"Edad: {resultado.Edad}")
            print(f"Correo: {resultado.Correo}")
            print(f"Cedula: {resultado.Cedula}")
        else:
            print("No se encontró un registro con esa cédula.")
#Se crea la opcion 3 la cual ejecuta la funcion de modificar
    elif opcion == '3':
        cedula = int(input("Ingrese la cedula del usuario que desea modificar: "))
        resultado = GD.Modificar_Datos(cedula)
#Se crea la opcion 4, esta permite eliminar un registro
    elif opcion == "4":
        cedula = int(input("Ingrese la cedula del usuario que desea eliminar: "))
        GD.Eliminar_Datos(cedula) 

#Se crea la opcion 5, sale del menu        
    elif opcion =="5": 
        print("Salida")
        break      
    else:
        print("Opcion no valida")