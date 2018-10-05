import qrcode  
import psycopg2
import os
#*****************************#
#*   Modulo hecho por        *#
#*	 gustavo saldivia    *#
#*			     *#
#*****************************#
class genqr () : 
	def __init__(self):

		self.conct = psycopg2.connect(database='iutrufino', user='postgres',
	                                    password='postgres', host='localhost')
		self.cur = self.conct.cursor()


	def consulta(self) :
		
	    self.cur.execute('SELECT * FROM diplomado;')
	    self.conct.commit()
	    self.rows = self.cur.fetchall()

	    print(self.rows)
	    return self.rows

	def generacion(self) : 
		self.data = self.consulta()
		for rows in self.data:
			cl = rows[0]
			cod = rows[1]
			img = qrcode.make('cod')
			f = open(cl+ "_" + cod + ".png", "wb")
			img.save(f)

		os.system('mv *.png -t qrs/')
	def cerrar_cursor():
		self.cur.close()
		self.conct.close()


