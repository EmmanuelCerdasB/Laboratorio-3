from msilib.schema import Class
from pickle import GLOBAL


global lista
lista = list()

class PAIS:
    def __init__(self):
        self.Cantidad_habitantes = 0
        self.idioma = ""
        self.fecha_idependencia = ""
        self.capita_MX = 0

    

        
# FUCION MX       
def Datos_MX():
    print("""-_-_-_-_-_-_ BIENVENIDOS A MEXICO  -_-_-_-_-
          
          """)

        
    Pais_MX = PAIS()
    
    Pais_MX.Cantidad_habitantes = float(input("Ingrese la Cantidad de habitantes: "))
    Pais_MX.idioma = input("Ingrese el Idioma: ")
    Pais_MX.fecha_idependencia = input("Ingrese la la fecha de idependencia: ")
    
    print("\n\rEl valor per cápita de Mexico: ", Pais_MX.Cantidad_habitantes*25*1.19)
        
    lista.append(Pais_MX)



# FUCION CR
def Datos_CR():
    print("""-         BIENVENIDOS A COSTA RICA          -
          
          """)
    
    Pais_CR = PAIS()
    
    Pais_CR.Cantidad_habitantes = float(input("Ingrese la Cantidad de habitantes: "))
    Pais_CR.idioma = input("Ingrese el Idioma: ")
    Pais_CR.fecha_idependencia = input("Ingrese la la fecha de idependencia: ")
    
    print("\n\rEl valor per cápita de Costa Rica: ", Pais_CR.Cantidad_habitantes*28*1.13)
    
    lista.append(Pais_CR)



# FUCION USA
def Datos_USA():
    print("""-         _WELCOME TO USA_          -
          
          """)

    
    Pais_USA = PAIS()
    
    Pais_USA.Cantidad_habitantes = float(input("Ingrese la Cantidad de habitantes: "))
    Pais_USA.idioma = input("Ingrese el Idioma: ")
    Pais_USA.fecha_idependencia = input("Ingrese la la fecha de idependencia: ")
    
    print("\n\rEl valor per cápita de USA: ", Pais_USA.Cantidad_habitantes*32*1.23)
    
    lista.append(Pais_USA)



# FUCION BR
def Datos_BR():
    print("""-_-_       BEM-VINDO AO BRASIL         _-_-
          
          """)

    
    Pais_BR = PAIS()
    
    Pais_BR.Cantidad_habitantes = float(input("Ingrese la Cantidad de habitantes: "))
    Pais_BR.idioma = input("Ingrese el Idioma: ")
    Pais_BR.fecha_idependencia = input("Ingrese la la fecha de idependencia: ")
    
    print("\n\rEl valor per cápita de Brasil: ", Pais_BR.Cantidad_habitantes*18*1.26)
    
    lista.append(Pais_BR)
    



# FUCION MENU
def menu():
    opcion = 0

    while opcion != 5:
        opcion = int(input("""
                __Selecione su pais__
                
       1- MX                                  | 
       2- CR                                  | 
       3- USA                                 | 
       4- BR                                  | 
       5- Salir                               | 
       
       """))

        if opcion == 1:
            Datos_MX()
        
        elif opcion == 2:
            Datos_CR()
        
        elif opcion == 3:
            Datos_USA()
            
        elif opcion == 4:
            Datos_BR()
        
        elif opcion == 5:
            print("Programa finalizado, gracias")
    

menu()
















