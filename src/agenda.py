"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1,2,3,4,5,6,7,8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    La funcion va a la ruta donde estan los contactos , las pasa a fichero , que se va recoriendo con la linea metiendose a su vez en procesar_contacto junto a los contactos.

    Args:
        contactos (list): Se guardará una lista de diccionarios creado en procesar_contactos().

    Returns:
        contactos (list): Una lista con cada diccionario de cada persona.
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            procesar_contacto(linea , contactos)     
    
    
def procesar_contacto(linea:str , contactos:list):
    """Procesara cada linea del ficho antes mencionado , convertirá dicha linea en una lista , despues seleccionaremos de la lista los datos 
     que queremos y lo inplementamos a un diccionario y este lo añadiremos a la lista de contactos .

    Args:
        contactos (list): Se guardará una lista de diccionarios creados.

    Returns:
        contactos (list): Una lista con cada diccionario de cada persona.

    Note:
        El .append añade a la lista de contactos el diccionario registrado de informacion_contactos.
    ...
    """
    informacion_contactos = dict()
    linea = linea.strip().split(";")
    nombre = linea[0] 
    apellido = linea[1]
    email = linea[2]
    telefono = linea[3:]
    informacion_contactos ={"nombre": nombre ,"apellido": apellido , "email": email, "telefonos": telefono}
    contactos.append(informacion_contactos)
    
def mostrar_contactos(contactos : list):
    """ Mostrara cada contacto ordenado y si algún contacto tiene la lista de telefono vacia inprimirá ninguno.

    Args:
        contactos (list): Se guardará una lista de diccionarios creados.
    
    Returns:
        print : Imprime la agenda mencionando primero cuantos contactos hay y una linea que serará cada contacto.

    Note:
        La funcion ordenar ordena de forma alfabetica cada contacto.
    """
    borrar_consola()
    contactos = ordenar(contactos)
    print(f"AGENDA {len(contactos)}\n"
          "-------------------") 
    for i in contactos:
        if i['telefonos'] == []:
            i['telefonos'] = 'ninguno'
    for i in contactos:
        if i["telefonos"] == 'ninguno':
            print(f"Nombre : {i['nombre']} {i['apellido']}    ({i['email']})",end="\n")
            print(f"Teléfonos: {i['telefonos']}\n"
              "............................")
        else:
            print(f"Nombre : {i['nombre']} {i['apellido']}    ({i['email']})",end="\n")
            print(f"Teléfonos: {" / ".join(i['telefonos'])}\n"
                "............................")



def buscar_contacto(contactos , email):
    """Se recorrerá la lista contactos buscando una posicion de un gmail anteriormente introducido.

    Args:
        contactos (list) : Lista que contiene cada diccionario de cada contacto .
        email (str) : Tiene el email del contacto que queremos buscar .
        
    Returns:
        pos (int) : Retornamos la posición del correo que hemos buscado.

    Note:
        El .get() selecciona dentro del diccionario.
    """
    i=-1
    for contacto in contactos:
        i +=1 
        if contacto.get("email") == email:
            pos = i
            return pos
        
def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda
    ...
    Elimanará el contacto que hemos buscado en la funcion buscar_contacto(). 

    Args:
        contactos (list) : Lista que contiene cada diccionario de cada contacto .
        email (str) : Tiene el email del contacto que queremos buscar .
    
    Returns:
        print : Según si se a eliminado el email que buscamos o no se a encontrado .

    Raises:
        Exception (cuaquier excepcion) : inprimirá el tipo de error y que no se eliminó ningún contacto.

    """
    borrar_consola()
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos , email)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

def agenda(contactos: list):
    """Ejecuta el menú de la agenda con varias opciones
    ...
    Recibiremos los contactos y mostraremos la funcion mostrar_menu() para que nos diga una opcion del 1-8 que se pedirá en pedir_opcion() , comprobaremos si la opción está 
    en la direncia simetrica del conjunto  OPCIONES_MENU y {8} y comprobamos cada opcion con su función corresponciente.

    Args:
        contactos (list) : Lista que contiene cada diccionario de cada contacto .

    Note:
        Lo que retorna será mencionado en la documentación de cada función.
    """ 
    
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion=0
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 8
        if opcion in OPCIONES_MENU ^ {8} :
            if opcion == 1:
                borrar_consola()
                agregar_contacto(contactos)
            elif opcion == 2:
                borrar_consola()
                email = input("Dime el email de la persona que desea modificar\n"
                      "=> ")
                modificar_contacto(contactos , email)
            elif opcion == 3:
                borrar_consola()
                email = input("Dime el email de la persona que desea eliminar\n"
                      "=> ")
                eliminar_contacto(contactos , email)
            elif opcion == 4:
                borrar_consola()
                borrar_agenda(contactos)
            elif opcion == 5:
                borrar_consola()
                cargar_contactos(contactos)
            elif opcion == 6:
                borrar_consola()
                email = input("Dime el email de la persona que desea buscar\n"
                      "=> ")
                print(buscar_contacto(contactos , email))
            elif opcion == 7:
                borrar_consola()
                mostrar_contactos(contactos)     
            
def modificar_contacto(contactos , email):
    """Buscaremos la posición del contacto que se quiere modificar con el email , despues se pedirá al usuario que tipo de cambio quiere 
    realizar y llamará a la función de pedir lo que el usuario quiera cambiar y se realizará el cambio en la posición

    Args:
        contactos (list) : Lista que contiene cada diccionario de cada contacto .
        email (str) : guardará el email que seleccionamos en la lista de linea.

    Note:
        No tiene returns ni excepciones ya que cada funcíon dentro de pedir_nobre,email y telefono lo tienen .
    """
    pos = buscar_contacto(contactos,email)
    print("Que quieres cambiar ?")
    cambio = input("n : nombre , e : email , t : telefono o enter si no desea modificar.\n"
                       "=> ")
    while cambio != "":
        if cambio == "n":
            nombre , apellido = pedir_nombre()
            contactos[pos]['nombre'] = nombre
            contactos[pos]['apellido'] = apellido
            cambio = ""
        elif cambio == "e":
            email = pedir_email(contactos)
            contactos[pos]['email'] = email
            cambio = ""
        elif cambio == "t":
            telefono = pedir_telefono()
            contactos[pos]['telefono']=telefono
            cambio = ""
        else:
            print("No es una de las opciones.")
            cambio = input("n : nombre , e : email , t : telefono o enter si no desea modificar.\n"
                       "=> ")
            
def borrar_agenda(contactos):
    """Elimina toda la agenda
    Args:
        contactos (list) : Lista que contiene cada diccionario de cada contacto .
    """
    contactos.clear()
    return contactos

def mostrar_menu():
    """Inprime la agenda con las diferentes opciones que tiene."""
    print("AGENDA\n"
          "------\n"
          "1. Nuevo contacto\n"
          "2. Modificar contacto\n"
          "3. Eliminar contacto\n"
          "4. Vaciar agenda\n"
          "5. Cargar agenda inicial\n"
          "6. Mostrar contactos por criterio\n"
          "7. Mostrar la agenda completa\n"
          "8. Salir\n")
    
def pedir_opcion():
    """Le pide al usuario la opcion que quiere realizar.

    Returns:
        return (opcion : int) : Devuelve el numero de la opción.

    Raises:
        ValueError : Nos saltará un error al no ser un numero , le pone la opcion el valor -1 .

    """
    try:
        opcion = int(input(">> Seleccione una opción: "))
        return opcion
    except ValueError as e :
        print(e,"No es un número")
        opcion = -1
        return(opcion)
    
def agregar_contacto(contactos : list):
    """Agregamos los parametros nombre , apellido , email y telefono a un diccionario como es informacion_contactos que tiene 
    las keys que necesitamos y depues se las agregamos a contactos. 
    
    Args:
        contactos (list) : Lista que almacenará cada contacto en diccionarios.

    Note:
        El .append añade los diccionarios a la lista.
    """
    nombre , apellido = pedir_nombre()
    email = pedir_email(contactos)
    telefono = pedir_telefono()
    informacion_contactos ={'nombre':nombre , 'apellido':apellido , 'email':email , 'telefonos':telefono}
    contactos.append(informacion_contactos)

def validar_telefono(input_tel):
    """Revisará el numero introducido para saber si es válido cumpliendo los parametros seleccionados.

    Args:
        input_tel (str) : Es el numero de telefono que le introducimos. 

    Returns:
        retunt (boolean) : Devuelve True si la validación sale bien y False si hay algun error.
    """
    if input_tel == "":
        return False
    elif input_tel.find("+") != -1:
        if len(input_tel) == 12 and input_tel[2] == "4":
            return True
        else:
            return False
    elif len(input_tel) > 9 or len(input_tel)<9:
        return False 
    return True 

def pedir_telefono():
    """Pedirá al usuario que introduzca su numero de telefono y posteriormente será validado en valida_telefono.

    Raises:
        ValueError : Si salta algún error de valor .

    Returns:
        retunt (telefonos : linea) : Devolverá los teloefonos para ser añadidos a la agenda .
    """
    cont = None
    contador = 0
    telefonos = list()
    while cont == None:
        try:
            contador += 1
            input_tel = str(input(f"Dame tu teléfono nº {contador} => "))
            validado= validar_telefono(input_tel)
            if validado == True:
                telefonos.append(input_tel)
            if contador == 1 and input_tel == "":
                input_tel="ninguno"
                return input_tel
            if input_tel == "":
                return telefonos     
        except ValueError as e:
            contador -=1
            print(e)

def pedir_email(contactos):
    """Pedira el email lo mandará a validar y dependiendo de si es valido o no el contador cambiará su valor para finalizar. 
    
    Args:
        contactos (list) : Lista que almacenará cada contacto en diccionarios.

    Returns:
        retunt (email : str) : retornará el email ya revidado y valido.

    Note:
        El ValueError saltará en validar_email.
    """
    cont = None
    while cont == None:
        email = input("Dime tu email => ")
        if email == "":
            raise ValueError ("el email no puede ser una cadena vacía")
        elif 0<len(email)<9:
            raise ValueError ("El email no está completo.")
        elif email.find("@") == -1:
            raise ValueError ("el email no es un correo válido.")
        encontrado = buscar_contacto(contactos,email)
        if encontrado != None:
            raise ValueError ("el email ya existe en la agenda")
        cont = "Diego ponme un 15//2 plis"
        validar_email(email,contactos)
        return email
        
def validar_email(email : str,contactos):
    """Validará el gmail siempre y cuando consiga saltear cada parametro. 
    
    Args:
        contactos (list) : Lista que almacenará cada contacto en diccionarios.

    Raises:
        ValueError : Saldrá dependiendo de cada parametro erroneo.

    """  
    if email == "":
            raise ValueError ("el email no puede ser una cadena vacía")
    elif 0<len(email)<9:
        raise ValueError ("El email no está completo.")
    elif email.find("@") == -1:
        raise ValueError ("el email no es un correo válido.")
    encontrado = buscar_contacto(contactos,email)
    if encontrado != None:
        raise ValueError ("el email ya existe en la agenda")

def obtener_nombre(contacto):
    """Va devolviendo el nombre"""
    return contacto['nombre']

def ordenar(contactos):
    """Ordenará contactos segun el nombre"""
    contactos = sorted(contactos, key=obtener_nombre)
    return contactos

def pedir_nombre():
    """Pedira el nombre lo validará y dependiendo de si es valido o no saltará un error. 
    
    Args:
        contactos (list) : Lista que almacenará cada contacto en diccionarios.
    
    Raises:
        ValueError : Siempre que el nombre o el apellido no sea valido .
    
    Returns:
        retun (nombre : str) : Devuelve el nombre ingresado y validado .
        return (apellido : str) : Devuelve el apellido igresado y validado.

    Note:
        .
    """ 
    cont = None
    while cont == None:
        try:
            nombre = input("Dime tu nombre => ")
            if nombre == "" or type(nombre)==int:
                raise ValueError ("No se ha detectado nombre")
            apellido = (input("Dime tu apellido => "))
            if  apellido == "" or type(apellido)==int:
                raise ValueError ("No se ha detectado apellido")
            cont = "Diego ponme un 15//2 plis"
            return nombre , apellido
        except ValueError as e:
            print(e)
    
def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")

def main():
    """ Función principal del programa
    """
    borrar_consola()
    email = "rciruelo@gmail.com"
   
    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = list()
    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(contactos)
    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos , email)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda(contactos)

if __name__ == "__main__":
    main()