import psycopg2
##################################
#Modulo hecho por Gustavo Saldivia#
##################################


""" 
crear la base de datos primero
"""
class creacion():
    def __init__(self):
        self.conct=psycopg2.connect(database = 'iutrufino' , user = 'postgres',
                                        password='postgres',host='localhost')
        self.cur = self.conct.cursor()


    def crear_tables(self):
        comandos = ("""
                create table alumno(
                nombre varchar(80),
                apellido varchar(80),
                especialidad varchar(80)
                )
                """,
            """
                create table diplomado(
                cod_diplomado varchar(80)
                )
            """
            )
        for i in comandos:
                self.cur.execute(i)
        self.conct.commit()
        self.cur.close()



class recoleccion():
    def __init__(self):

        self.conct = psycopg2.connect(database='iutrufino', user='postgres',
                                        password='postgres', host='localhost')
        self.cur = self.conct.cursor()

    def obtener_datos(self):
        try:
            
           
            self.datosc = ['nombre','apellido','especialidad']
            print("introduzca en ese orden : ","\n", self.datosc)
            self.datos = [str(input("--> "))  for i in range(len(self.datosc))]
            self.dat2 = str(self.datos);self.dat2=self.dat2.replace('[','');self.dat2=self.dat2.replace(']','')
            print(self.dat2)
            self.cur.execute ("INSERT INTO alumno(nombre,apellido,especialidad)values(%s);"%self.dat2 )
            self.conct.commit()

            
        except Exception as e:
            print("""debe introducir todos los datos para que funcione""",e)


        
    def consulta(self) :
        

        self.cur.execute('SELECT * FROM alumno;')
        self.rows = self.cur.fetchall()
        print(self.rows)
        self.conct.commit()
    

    def consulta_nombre(self, nombre):
        
        self.cur.execute("SELECT * FROM alumno WHERE nombre = '%s'" %nombre)

        self.rows = self.cur.fetchall()  
        print(self.rows)      
        self.conct.commit()
        



    def consulta_cedula(self, cedula):
        
        self.cur.execute('SELECT * FROM alumno WHERE cedula= "%s"'%cedula)
        self.conct.commit()

    def eliminacion_por_nombre(self,nombre):
        
        self.cur.execute('DELETE  FROM alumno WHERE nombre= "%s"'%nombre)
        self.conct.commit()
    def consulta_cedula(self, cedula):

        self.cur.execute('DELETE alumno WHERE cedula= "%s"'%cedula)
        self.conct.commit()

    def cerrar_consulta():
        self.cur.close()
        self.conct.close()
"""x = recoleccion()
x.obtener_datos()
x.consulta()"""
