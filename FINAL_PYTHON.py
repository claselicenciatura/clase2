from pylab import *
import MySQLdb

def DESCONECTAR():
    db.close()
    exit

def TODOS():
    cursor = db.cursor()
    sql = "SELECT * FROM ALUMNOS" # CONSULTA DE TODOS LOS DATOS DE LA TABLA ALUMNOS
    try:
       cursor.execute(sql)# EJECUTA EL COMANDO SQL
       resultados = cursor.fetchall()# MUESTRA LAS FILAS DE LA LISTA
       for row in resultados:
          print "Carnet: " , row[0]
          print "Nombre: ", row[1]
          print "Apellido: ", row[2]
          print "Matematica: ", row[3]
          print "Literatura: ", row[4]
          print "Programacion: ", row[5]
          print "Quimica: ", row[6]
          print "Ingles: ", row[7]
          print "\n************************************"
       resultados = cursor.fetchall()

    except:
       print "No hay registros"


def REGISTRAR():
    Carne = raw_input("Ingrese el Carnet: ")
    Nombre = raw_input("Ingrese el Nombre: ")
    Apellido = raw_input("Ingrese el Apellido: ")
    Matematica= raw_input("Ingrese Nota de Matematica: ")
    Literatura= raw_input("Ingrese Nota de Literatura: ")
    Programacion= raw_input("Ingrese Nota de Programacion: ")
    Quimica= raw_input("Ingrese Nota de Quimica: ")
    Ingles= raw_input("Ingrese Nota de Ingles: ")
    # Preparar consulta SQL para insertar un registro en la base de datos.
    sql = "INSERT INTO ALUMNOS(Carne, Nombre, Apellido, \
           Matematica, Literatura, Programacion, Quimica, Ingles) \
           VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s')" % \
           (Carne, Nombre, Apellido, Matematica, Literatura, Programacion, Quimica, Ingles )

    try:
        cursor.execute(sql)# Ejecuta el comando SQL
        db.commit()# Confirma los cambios en la base de datos
    except:
        print "error" # Deshacer cualquier cosa si hay error
        db.rollback()

def CONSULTARc(C):
    sql = "SELECT * FROM ALUMNOS WHERE Carne = %s" % C
    try:
       cursor.execute(sql) # Ejecuta el comando SQL
       # MUESTRA LAS FILAS DE LA LISTA resultados
       resultados = cursor.fetchall()# MUESTRA LAS FILAS DE LA LISTA
       for row in resultados:
          print "Carnet: " , row[0]
          print "Nombre: ", row[1]
          print "Apellido: ", row[2]
          print "Matematica: ", row[3]
          print "Literatura: ", row[4]
          print "Programacion: ", row[5]
          print "Quimica: ", row[6]
          print "Ingles: ", row[7]
          print "\n************************************"
       resultados = cursor.fetchall()

    except:
       print "El carnet ingresado no pertenece a ningun alumno"


def CONSULTARn():
    Nombre = raw_input("Ingrese el Nombre del estudiante del que desea consultar entre comillas: ")
    sql = "SELECT * FROM ALUMNOS WHERE Nombre = %s" % Nombre
    try:
       cursor.execute(sql) # Ejecuta el comando SQL
       # MUESTRA LAS FILAS DE LA LISTA resultados
       resultados = cursor.fetchall()# MUESTRA LAS FILAS DE LA LISTA
       for row in resultados:
          print "Carnet: " , row[0]
          print "Nombre: ", row[1]
          print "Apellido: ", row[2]
          print "Matematica: ", row[3]
          print "Literatura: ", row[4]
          print "Programacion: ", row[5]
          print "Quimica: ", row[6]
          print "Ingles: ", row[7]
          print "\n************************************"
       resultados = cursor.fetchall()

    except:
       print "No se encontro el nombre de alumano ingresado"


def GRAFICAR():
    Lista=[]
    Etiquetas=["Matematica", "Literatura", "Programacion", "Quimica", "Ingles"]
    Carne = raw_input("Ingrese el Carnet del alumno que desea consultar: ")
    sql = "SELECT Matematica, Literatura, Programacion, Quimica, Ingles FROM ALUMNOS WHERE Carne = %s" % Carne
    try:
        cursor.execute(sql)
        registro = cursor.fetchone()

        for row in range (len(registro)):
            dato=int (registro[row])
            Lista.append(dato)
        registro = cursor.fetchone()
        print Lista

        # grafica de barras

        xlocations = array(range(len(Lista)))+0.40 #arreglo para eje x
        width = 0.10 #Mide el ancho de la barra

        bar(xlocations, Lista,  width=width)

        xticks(xlocations+ width/2, Etiquetas) #donde quedan las etiquetas eje x
        xlim(0, xlocations[-1]+width*2)
        title("*****---GRAFICAS DE LAS NOTAS---*****")

        show()
    except:
        print "No se encontro"


def ACTUALIZAR():
    Carne = raw_input("Ingrese el Carnet del alumno que desea consultar: ")
    CONSULTARc(Carne)
    print "Que nota desea modificar?"
    print "1- Matematica"
    print "2- Literatura"
    print "3- Programacion"
    print "4- Quimica"
    print "5- Ingles"
    op=raw_input("")
    if op=="1":
        Matematica=raw_input("Escriba la nueva nota: ")
        sql = "UPDATE ALUMNOS SET Matematica = '%s' \
                          WHERE Carne = '%s' " \
                          % (Matematica, Carne)
        try:
           cursor.execute(sql) # Ejecutar comando
           db.commit()# Confirmar los cambios en la base de datos
        except:
           db.rollback()# No hacer nada si hay error
    if op=="2":
        Literatura=raw_input("Escriba la nueva nota: ")
        sql = "UPDATE ALUMNOS SET Literatura = '%s' \
                          WHERE Carne = '%s' " \
                          % (Literatura, Carne)
        try:
           cursor.execute(sql) # Ejecutar comando
           db.commit()# Confirmar los cambios en la base de datos
        except:
           db.rollback()# No hacer nada si hay error
    if op=="3":
        Programacion=raw_input("Escriba la nueva nota: ")
        sql = "UPDATE ALUMNOS SET Programacion = '%s' \
                          WHERE Carne = '%s' " \
                          % (Programacion, Carne)
        try:
           cursor.execute(sql) # Ejecutar comando
           db.commit()# Confirmar los cambios en la base de datos
        except:
           db.rollback()# No hacer nada si hay error
    if op=="4":
        Quimica=raw_input("Escriba la nueva nota: ")
        sql = "UPDATE ALUMNOS SET Quimica = '%s' \
                          WHERE Carne = '%s' " \
                          % (Quimica, Carne)
        try:
           cursor.execute(sql) # Ejecutar comando
           db.commit()# Confirmar los cambios en la base de datos
        except:
           db.rollback()# No hacer nada si hay error
    if op=="5":
        Ingles=raw_input("Escriba la nueva nota: ")
        sql = "UPDATE ALUMNOS SET Ingles = '%s' \
                          WHERE Carne = '%s' " \
                          % (Ingles, Carne)
        try:
           cursor.execute(sql) # Ejecutar comando
           db.commit()# Confirmar los cambios en la base de datos
        except:
           db.rollback()# No hacer nada si hay error



#PROGRAMA PRINCIPAL

#CONECTARSE A UN SERVIDOR
servidor=raw_input("Cual es el nombre del servidor al que se conectara? ")
cuenta=raw_input("Cual es el nombre de usuario para conectarse? ")
contra=raw_input("Cual es el password de la cuenta? ")
BaseDatos=raw_input("Que nombre tiene la base de datos a conectar? ")
db = MySQLdb.connect(servidor,cuenta,contra,BaseDatos )
cursor = db.cursor()


def MENU():
    print "**********BIENVENIDOS AL SISTEMA**********\n"
    print "**********COMPUTACION INFORMATICA**********"
    print "********************MENU********************"
    print "1- Agregar un alumno a la base de datos"
    print "2- Consultar todos los alumnos"
    print "3- Consultar un alumno por su carnet"
    print "4- Consultar un alumno por su nombre"
    print "5- Ver grafica de alumno"
    print "6- Modificar las calificaciones de un alumno"
    print "7- Finalizar la gestion de base de datos"
    op=raw_input()
    while op<>"7":
        if op=="1":
            REGISTRAR()
        if op=="2":
            TODOS()
        if op=="3":
            Carne = raw_input("Ingrese el Carnet del alumno que desea consultar: ")
            CONSULTARc(Carne)
        if op=="4":
            CONSULTARn()
        if op=="5":
            GRAFICAR()
        if op=="6":
            ACTUALIZAR()
        if op=="7":
            DESCONECTAR()

        print "\n\n\n\n*****************MENU*****************"
        print "1- Agregar un alumno a la base de datos"
        print "2- Consultar todos los alumnos"
        print "3- Consultar un alumno por su carnet"
        print "4- Consultar un alumno por su nombre"
        print "5- Ver grafica de alumno"
        print "6- Modificar las calificaciones de un alumno"
        print "7- Finalizar la gestion de base de datos"
        op=raw_input()

MENU()



















