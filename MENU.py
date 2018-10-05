import MOD1.MOD1 as rec
import MOD2.MOD2 as genqr
import os,sys
x = rec.recoleccion()
create = rec.creacion()
Gqr = genqr.genqr()
def crear_tables():
    create.creacion()
def cargar():
    x.obtener_datos()
def consultar() :
    x.consulta()
def consultar_nombre(nombre) : 
    x.consulta_nombre(nombre)
def consultar_cedula():
    pass
def cerrar_consultas():
    x.cerrar_consulta()
def generar_qrs():
    Gqr.generacion()




       #***************************************
       #*	Desarrollado por Gustavo      *
       #*	Saldivia ver 0.1 	      *
       #***************************************

def banner():
	os.system('clear')
	print ( """

██████╗ ██╗██████╗ ██╗      ██████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██║██╔══██╗██║     ██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║██████╔╝██║     ██║   ██║██╔████╔██║███████║██║  ██║██║   ██║███████╗
██║  ██║██║██╔═══╝ ██║     ██║   ██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║╚════██║
██████╔╝██║██║     ███████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                
                     █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗                    
                    ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║                    
                    ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║                    
                    ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║                    
                    ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║                    
                    ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝  
                                    ver 0.9                  
                                                                                

	""")


def menu ():
    desc = False
    x = 0
    while desc == False :
        banner()
        #xd = rec.recoleccion.conectar
        print("Funciones disponibles : 1 cargar, 2 consultar, 3 borrar, 4 generar qr,5 crear tablas")
        print("Introduzca la funcion a realizar")
        try:
            x = int(input('-->'))
        except Exception as e:
            print("Debe tipear correctamente , 1 cargar, 2 consultar, 3 borrar")
            continue
        if x==5 : 
            create.crear_tables()

        if x == 4 : 
            generar_qrs()
        if x ==  3 :
            pass
        if x == 2 :   
            x_consulta = 0
            print("quiere consultar por nombre? presione 2")
            print("quiere consultar por cedula? presione 1")
            print("quiere consultar general? presione 3")
  
            x_consulta = int(input('consulta por? -->'))
            if x_consulta == 1 :
                consultar_cedula(str(input("inroduce la cedula")))
            if x_consulta == 2 :
                consultar_nombre(str(input("introduce el nombre")))
            if x_consulta == 3:
                consultar()
        if x == 1 :
            cargar()
        print("Desea realizar otra accion?, tipee salir para finalizar")
        x = input("-->")
        if x == 'salir':
            cerrar_consultas()
            desc = True
            Gqr.cerrar_cursor()
        else :
            pass

menu()





