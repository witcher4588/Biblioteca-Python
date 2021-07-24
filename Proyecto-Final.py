import csv
from datetime import datetime
from datetime import timedelta

identificacion=[]
nombre=[]
primerApellido=[]
segundoApellido=[]
correoElectronico=[]


autor=[]
titulo=[]
estado=[]
fechaPrestamo=[]
fechaDevolucion=[]
dueñoActual=[]
libros={}


def actualizaArchivoPersona():
    
    nombre.clear()
    identificacion.clear()
    primerApellido.clear()
    segundoApellido.clear()
    correoElectronico.clear()
    with open("personas.csv",'r') as archivo:
        lector = csv.reader(archivo, delimiter =';')
        
            
    
        for x in lector: 
            
            identificacion.append(x[0]) 
            nombre.append(x[1]) 
            primerApellido.append(x[2]) 
            segundoApellido.append(x[3]) 
            correoElectronico.append(x[4]) 
            
            
    archivo.close()

def actualizarLibros():
    autor.clear()
    titulo.clear()
    estado.clear()
    fechaPrestamo.clear()
    fechaDevolucion.clear()
    
   
    with open("Libros.csv",'r',newline='') as archivoLibro:
                
                lector = csv.DictReader(archivoLibro,delimiter=";",fieldnames=["Autor","Titulo","Estado","Fecha de Prestamo","Fecha de Devolucion","Dueño Actual"])
                
                key=0
                
                for x in lector:
                    libros[key] = {}
                    libros[key]["Autor"]=x["Autor"]
                    libros[key]["Titulo"]=x["Titulo"]
                    libros[key]["Estado"]=x["Estado"]
                    libros[key]["Fecha de Prestamo"]=x["Fecha de Prestamo"]
                    libros[key]["Fecha de Devolucion"]=x["Fecha de Devolucion"]
                    libros[key]["Dueño Actual"]= x["Dueño Actual"]
                   
                              
                    key = key + 1
    archivoLibro.close()



def verPersonas():
        
    temporalTodo=[]
            
     
       
    temporalTodo.append(identificacion[1:len(identificacion)])    
    temporalTodo.append(nombre[1:len(nombre)])
    temporalTodo.append(primerApellido[1:len(primerApellido)])    
    temporalTodo.append(segundoApellido[1:len(segundoApellido)])
    temporalTodo.append(correoElectronico[1:len(correoElectronico)])
    
     
    
    z=0
    
    print("\n%-25s %-35s %-25s %-25s %-25s" %("IDENTIFICACION", "NOMBRE", "PRIMER APELLIDO", "SEGUNDO APELLIDO", "CORREO ELECTRONICO\n"))
    for x in temporalTodo[0]:
          
        print("%-25s %-35s %-25s %-25s %-25s" %(temporalTodo[0][z],temporalTodo[1][z],temporalTodo[2][z],temporalTodo[3][z],temporalTodo[4][z]))
                      
        z = z + 1    
    
    
    input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
    return main() 
    

def ordenarLista():
    
    identificacionDesordenados=[]
    nombresDesordenados=[] 
    primerApellidoDesordenados=[]
    segundoApellidoDesordenados=[]
    correoElectronicoDesordenados=[] 
    
    
    
    
    identificacionOrdenados=[]
    nombresOrdenados=[] 
    primerApellidoOrdenados=[]
    segundoApellidoOrdenados=[]
    correoElectronicoOrdenados=[] 
    
    

    
    
    nombresDesordenados.append((nombre[1:len(nombre)])) 
    
    identificacionDesordenados.append((identificacion[1:len(identificacion)]))
    primerApellidoDesordenados.append((primerApellido[1:len(primerApellido)]))
    segundoApellidoDesordenados.append((segundoApellido[1:len(segundoApellido)]))
    correoElectronicoDesordenados.append((correoElectronico[1:len(correoElectronico)])) 
    
    
    

    
    nombresOrdenados=sorted(nombresDesordenados[0])
    
    
    k = 0 
    while k != len(nombresOrdenados):
        for x in nombresDesordenados[0]: 
            if k < len(nombresOrdenados)  and nombresOrdenados[k] == x:
                            
                
              
                identificacionOrdenados.append(identificacionDesordenados[0][nombresDesordenados[0].index(x)])
                primerApellidoOrdenados.append(primerApellidoDesordenados[0][nombresDesordenados[0].index(x)])
                segundoApellidoOrdenados.append(segundoApellidoDesordenados[0][nombresDesordenados[0].index(x)])
                correoElectronicoOrdenados.append(correoElectronicoDesordenados[0][nombresDesordenados[0].index(x)])
                
                      
            
        k = k+1
    
       
    todoOrdenado=[]
    todoOrdenado.append(identificacionOrdenados)
    todoOrdenado.append(nombresOrdenados)
    todoOrdenado.append(primerApellidoOrdenados)
    todoOrdenado.append(segundoApellidoOrdenados)
    todoOrdenado.append(correoElectronicoOrdenados)
    
    
   
            
     
      
    
    
    z=0
    
    print("\n%-25s %-35s %-25s %-25s %-25s" %("IDENTIFICACION", "NOMBRE", "PRIMER APELLIDO", "SEGUNDO APELLIDO", "CORREO ELECTRONICO\n"))
    for x in todoOrdenado[0]:
          
        print("%-25s %-35s %-25s %-25s %-25s" %(todoOrdenado[0][z],todoOrdenado[1][z],todoOrdenado[2][z],todoOrdenado[3][z],todoOrdenado[4][z]))
                      
        z = z + 1    
        
        
    orden= input("\n::::::::::: Quieres que actualice la base de datos alfabeticamente también ? :::::::::::\n\n1- Si\n2- No\n\n---> ")    
        
    if orden == "1": 
            
        
        
        nuevoOrden= {} 
        
        
        for k in range(0,len(nombresOrdenados)-1):        
            nuevoOrden[k]={} 
            nuevoOrden[k]["Identificacion"] = todoOrdenado[0][k]
            nuevoOrden[k]["Nombre"] = todoOrdenado[1][k]
            nuevoOrden[k]["Primer Apellido"] = todoOrdenado[2][k]
            nuevoOrden[k]["Segundo Apellido"] = todoOrdenado[3][k]
            nuevoOrden[k]["Correo Electronico"] = todoOrdenado[4][k] 
            
    
        
    
        
        
        
        
    

        
        with open("personas.csv",'w+',newline='') as archivotest:
                
            escritor = csv.DictWriter(archivotest,delimiter=";",fieldnames=["Identificacion","Nombre","Primer Apellido","Segundo Apellido","Correo Electronico"])
            escritor.writeheader()   
            
            for x in range(0,len(nuevoOrden)-1):
                
                escritor.writerow(nuevoOrden[x])
            archivotest.close() 
            
        print("\n:::::::::::::::: BASE DE DATOS REORDENADA CON EXITO :::::::::::::\n")   
        
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main() 
    
    elif orden == "2":
           
        
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n")
        return main() 
    
    elif orden != "2" and orden != "1": 
        print("\nEsa opcion no es valida\n")
        input()
        return ordenarLista()         
        

def buscando():
    
    
    buscar = input("Hola, ingresa el nombre de la persona que deseas buscar ----- > ").capitalize()
    
    encontrado = 0
    temporal=[]
      
   

    
    
    for x in nombre: 
                
         
        check = x.split() 
        for k in check: 
            if buscar == k:
                encontrado += 1
                temporal.append(nombre.index(x))
        
                      
    if encontrado > 1: 
      print("\nEncontre mas de un resultado con ese nombre : \n")  
      for x in temporal: 
         print(f"{encontrado} - {nombre[x]}  {primerApellido[x]} {segundoApellido[x]}\n")
      
         encontrado = encontrado - 1 
      eleccion = int(input("Escribe el numero de la persona que deseas ver de la lista ---> "))
      
      print(f"\n :::::: Datos de {nombre[temporal[-eleccion]]} ::::::\n")
      
       
      
      print(f"\nIdentificacion: {identificacion[temporal[-eleccion]]}\nNombre: {nombre[temporal[-eleccion]]}\nPrimer Apellido: {primerApellido[temporal[-eleccion]]}\nSegundo Apellido: {segundoApellido[temporal[-eleccion]]}\nCorreo Electronico: {correoElectronico[temporal[-eleccion]]}\n" )
            
      temporal.clear()
      input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
      return main()
        
   
      
   
   
    elif encontrado == 1: 
         print(f"\n :::::: Datos de {nombre[temporal[0]]} ::::::\n")
         
                
         print(f"\nIdentificacion: {identificacion[temporal[0]]}\nNombre: {nombre[temporal[0]]}\nPrimer Apellido: {primerApellido[temporal[0]]}\nSegundo Apellido: {segundoApellido[temporal[0]]}\nCorreo Electronico: {correoElectronico[temporal[0]]}\n")
         temporal.clear()
         input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
         return main()
       
    
    
    
    elif encontrado == 0:
     print ("\n ---> Ese nombre no esta en la lista <---")
     noEncontrado()
   
        
def noEncontrado():
    
    opcionesValidas = ["1","2","0"]
    print(f"\n1- Buscar otra persona del registro\n2- Ingresar nueva persona en la lista\n\n0- Volver al menu principal\n")
    opcion = input()   
    
            
    if opcion=="1":
        buscando() 
    elif opcion == "2":
        return agregarPersona() 
    elif opcion == "0":
        return main()
    
    elif opcion not in opcionesValidas:
        print ("Esa opcion no es valida, porfavor vuelve a elegir una opcion")
        return noEncontrado()


def agregarPersona():
    nuevaPersona={}
    campos=["Identificacion","Nombre","Primer Apellido","Segundo Apellido","Correo Electronico"]
    datos=[]
    posicion = 0
    
   
    print("\n************ INGRESANDO NUEVA PERSONA **************")
    print("\nPorfavor ingresa los siguientes datos para la nueva persona : ")
    
    identificacion = input("*Identificacion ---> ")
    nombre= input("*Nombre ---> ").capitalize()
    erApellido= input("*Primer Apellido ---> ").capitalize()
    doApellido= input("*Segundo Apellido ---> ").capitalize()
    correo= input("Correo Electronico ---> ")
    

    
    
    if (identificacion or nombre or erApellido or doApellido) == "":
        print ("\n No puedes dejar en blanco los espacios con * ")
        return agregarPersona()
    elif (identificacion or nombre or erApellido or doApellido) != "":
        datos.append(identificacion)
        datos.append(nombre)
        datos.append(erApellido)
        datos.append(doApellido)
        datos.append(correo)
        
        
    
    while posicion < len(campos):
            for y in campos:
                nuevaPersona[y] = datos[posicion]
                posicion = posicion +1
    
               
                
                  
               
    confirmar(nuevaPersona)
  
       
def confirmar(nuevaPersona):
    print("\nRevisa los datos que ingresaste y confirma si son correctos\n")
    
    
     
    
    print("\n%-25s %-35s %-25s %-25s %-25s" %("IDENTIFICACION", "NOMBRE", "PRIMER APELLIDO", "SEGUNDO APELLIDO", "CORREO ELECTRONICO\n"))
    print("%-25s %-35s %-25s %-25s %-25s" %(nuevaPersona['Identificacion'],nuevaPersona['Nombre'],nuevaPersona['Primer Apellido'],nuevaPersona['Segundo Apellido'],nuevaPersona['Correo Electronico']))
                      
      
    
    
    """  
    print("Identificacion -- > ",nuevaPersona['Identificacion'])
    print("Nombre -- > ",nuevaPersona['Nombre'])
    print("Primer Apellido -- > ",nuevaPersona['Primer Apellido'])
    print("Segundo Apellido -- > ",nuevaPersona['Segundo Apellido'])
    print("Correo -- > ",nuevaPersona['Correo Electronico'])
    """
    
    eleccion = input("\n1- Son Correctos\n2- Quiero volver a ingresar los datos\n\n0- Volver al Menu Principal\n")
    
    if eleccion == "1":
    
        with open("personas.csv",'a+',newline='') as archivo:
            
            escritor = csv.DictWriter(archivo,delimiter=";",fieldnames=["Identificacion","Nombre","Primer Apellido","Segundo Apellido","Correo Electronico"])       
            escritor.writerow(nuevaPersona)
            archivo.close()
            
        
        print("\n::::::::::::::: NUEVA PERSONA AGREGADA CON EXITO :::::::::::::::\n")
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main()
        
        
    elif eleccion == "2":
        return agregarPersona()
    
    elif eleccion =="0":
        return main()
        
    elif eleccion != "1" and eleccion!="2":
        print("Esa opcion no es valida")
        confirmar(nuevaPersona)

def idenfiticate(nombreDeLibroPrestamo):
    
    
       
    
    temporalTodo=[]
    
    personaActual = []   
    
    temporalTodo.append(identificacion[1:len(identificacion)])    
    temporalTodo.append(nombre[1:len(nombre)])
    temporalTodo.append(primerApellido[1:len(primerApellido)])    
    temporalTodo.append(segundoApellido[1:len(segundoApellido)])
    temporalTodo.append(correoElectronico[1:len(correoElectronico)])
    opcionesValidas = []
    opcion = 1 
    
    for x in temporalTodo[0]: 
        opcionesValidas.append(opcion)
        opcion = opcion + 1
        
        
       
    
    z=0
    usuario=1
    print("\n::::: PRESIONA CUALQUIER TECLA PARA VER LA LISTA DE USUARIOS E IDENTIFICATE :::::\n")
    input()
    print("\n%-0s %-23s %-35s %-20s %-20s %-20s" %("#","IDENTIFICACION", "NOMBRE", "PRIMER APELLIDO", "SEGUNDO APELLIDO", "CORREO ELECTRONICO\n"))
    for x in temporalTodo[0]:
         
        print(usuario,"%-0s %-20s %-35s %-20s %-20s %-20s" %("  ",temporalTodo[0][z],temporalTodo[1][z],temporalTodo[2][z],temporalTodo[3][z],temporalTodo[4][z]))
                      
        z = z + 1
        usuario =  usuario + 1    
    
      
    soy = input("\n::::: Cual es tu número de lista ? :::::\n")
    
    if int(soy) not in opcionesValidas:
        print("\nEsa persona no esta en la lista, porfavor vuelve a ver la lista y elige tu nombre\n") 
        return (idenfiticate(nombreDeLibroPrestamo))
    
    
        
    print("\nEres",temporalTodo[1][int(soy)-1],temporalTodo[2][int(soy)-1],temporalTodo[3][int(soy)-1],"?") 
    confirmacion = input("1-Si\n2-No\n\n0- salir""\n --> ")
    opcionesValidas = ["1","2","0"]
    if confirmacion == "1" and nombreDeLibroPrestamo =="ninguno":
       for x in range(0,2): 
        personaActual.append(temporalTodo[1][int(soy)-1] +" "+temporalTodo[2][int(soy)-1]+" "+ temporalTodo[3][int(soy)-1])
        
        
               
        return (prestarLibroDeLista(personaActual))
    
    elif confirmacion == "1" and nombreDeLibroPrestamo != "ninguno":        
            
        personaActual.append(temporalTodo[1][int(soy)-1] +""+temporalTodo[2][int(soy)-1]+""+ temporalTodo[3][int(soy)-1])
        return prestarLibro(nombreDeLibroPrestamo,personaActual)            
        
    elif confirmacion == "2":
        print("Presiona alguna tecla para buscarte de nuevo")
        idenfiticate(nombreDeLibroPrestamo)
    
    elif confirmacion == "0":
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main() 
    
    elif confirmacion not in opcionesValidas:
        print("----> opcion invalida <----")
        return (idenfiticate(nombreDeLibroPrestamo))
    

            
def verTodosTitulosLibros(): 
            
    x = 1
    print("\n\n:::::::::::::: LIBROS DISPONIBLES EN LA BIBLIOTECA :::::::::::::::::\n\n")
    
    print("\n%-85s %-5s" %("Titulo", "Autor\n"))
    while x < len(libros):       
      print("%-85s %-5s" %(libros[x]["Titulo"],libros[x]["Autor"])) 
      x = x+1   
    
    input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
    return main()
     
def pedirNuevoLibro():
    respuesta = input("\nQuieres que la Biblioteca agregue un libro a la coleccion ?\n1- Si\n2- No \n--->  ")
    if respuesta == "2":
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main()
    
    
    elif respuesta == "1":
        nuevoLibro={}
        campos=["Autor","Titulo","Idioma","Genero"]
        datos=[]
        posicion = 0
        
    
        print("************ INGRESANDO NUEVA PETICION DE LIBRO **************")
        print("\nPorfavor ingresa los siguientes datos para la lista de pedidos : ")
        
                
        Autor = input("*Autor ---> ").capitalize()
        Titulo= input("*Titulo ---> ").capitalize()
        Idioma= input("*Idioma ---> ").capitalize()
        Genero= input("Genero ---> ").capitalize()
        
        

        
        
        if (Autor or Titulo or Idioma or Genero) == "":
            print ("\n No puedes dejar en blanco los espacios con * ")
            return pedirNuevoLibro()
        elif (Autor or Titulo or Idioma or Genero) != "":
            datos.append(Autor)
            datos.append(Titulo)
            datos.append(Idioma)
            datos.append(Genero)  
        
        
        
        while posicion < len(campos):
                for y in campos:
                    nuevoLibro[y] = datos[posicion]
                    posicion = posicion +1                   
                    
        print ("\n************ DATOS INGRESADOS **************\n")
        confirmarLibro(nuevoLibro)
        
        
    elif respuesta != "1" or respuesta != "2":
        print("\n Esa opcion no es valida")
        return pedirNuevoLibro()     
    
def confirmarLibro(nuevoLibro):
    
    
    print("\nRevisa los datos que ingresaste y confirma si son correctos\n")
    
      
    print("Autor -- > ",nuevoLibro['Autor'])
    print("Titulo -- > ",nuevoLibro['Titulo'])
    print("Idioma -- > ",nuevoLibro['Idioma'])
    print("Genero -- > ",nuevoLibro['Genero'])  
    
        
    
    eleccion = input("\n1- Son Correctos\n2- Quiero volver a ingresar los datos\n\n0- Volver al Menu Principal\n")
    
    if eleccion == "1":
    
        with open("Peticion_Libros_Nuevos.csv",'a+',newline='') as archivo:
            
            escritor = csv.DictWriter(archivo,delimiter=";",fieldnames=["Autor","Titulo","Idioma","Genero"])
            escritor.writerow(nuevoLibro)
            archivo.close()
            print(nuevoLibro) 
        print ("\n:::::::::::::: NUEVA PETICION INGRESADA CON EXITO AL WISHLIST :::::::::::::: \n")
                
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main()
    elif eleccion == "2":
        return pedirNuevoLibro()
    
    elif eleccion == "0":
        return main()
        
    elif eleccion != "1" and eleccion!="2" and eleccion != "0":
        print("Esa opcion no es valida")
        confirmarLibro(nuevoLibro)
    
def LibroNoEncontrado():
    
    print(f"\n1- Buscar otro libro del registro\n2- Ingresar una peticion de libro a la biblioteca\n\n0- Volver al menu principal\n")
    opcion=input()
    if opcion=="1":
         buscandoLibro() 
    elif opcion == "2":
        return pedirNuevoLibro() 
    elif opcion == "0":
          
         return main()
    elif opcion != "1" and opcion != "2" and opcion != "0" or opcion == "":
         print ("--> Esa opcion no es valida, porfavor vuelve a elegir una opcion <--")
         
         return LibroNoEncontrado()
  
def prestarLibroTiempo(tiempoPrestamo,sinLibro,personaActual):
           
    
    
        
    hoy = datetime.now()
    if tiempoPrestamo == 1:
        conteo = 15
        devolucion = hoy + timedelta(days=conteo)
        print (f'\nLa biblioteca te presta el libro "{sinLibro}" por 15 dias')
        print ("\nDebes devolver este libro para el ",devolucion.strftime("%d/%m/%Y"))
        
           
          
        
    elif tiempoPrestamo == 2:
        conteo = 30
        devolucion = hoy + timedelta(days=conteo)
        print (f'\nLa biblioteca te presta el libro "{sinLibro}" por 15 dias')
        print ("\nDebes devolver este libro para el ",devolucion.strftime("%d/%m/%Y")) 
        
        
    elif tiempoPrestamo == 3:
        conteo = 45
        devolucion = hoy + timedelta(days=conteo)
        print (f'\nLa biblioteca te presta el libro "{sinLibro}" por 15 dias')
        print ("\nDebes devolver este libro para el ",devolucion.strftime("%d/%m/%Y")) 
        
        
     
                
    
    diccionarioViejo={}    
    posicion = 0
    
    
        
    
       

    with open("Libros.csv",'r',newline='') as archivoLibro:
        
                
            
                lector = csv.DictReader(archivoLibro,delimiter=";")
                for x in lector: 
                 
                 diccionarioViejo[posicion] = {"Autor":(x['Autor']),"Titulo":(x['Titulo']),"Estado":(x['Estado']),"Fecha de Prestamo":(x['Fecha de Prestamo']),"Fecha de Devolucion":(x['Fecha de Devolucion']),"Dueño Actual":(x['Dueño Actual'])} 
                 posicion = posicion +1

                           
                
                for x in diccionarioViejo: 
                    
                    if diccionarioViejo[x]['Titulo']  == sinLibro: 
                        
                        
                        diccionarioViejo[x]['Estado'] = "Prestado"
                              
                   
                        diccionarioViejo[x]['Fecha de Prestamo'] = hoy.strftime("%d/%m/%Y") 
                                              
                       
                        diccionarioViejo[x]['Fecha de Devolucion'] = devolucion.strftime("%d/%m/%Y") 
                        
                        diccionarioViejo[x]['Dueño Actual'] = personaActual[0]
     
                       
    with open("Libros.csv",'w+',newline='') as archivoLibro:
                escritor = csv.DictWriter(archivoLibro,delimiter=";",fieldnames=["Autor","Titulo","Estado","Fecha de Prestamo","Fecha de Devolucion",'Dueño Actual'])
                escritor.writeheader()
                cuentaEntradas = (len(diccionarioViejo))
                cuenta=0
                while cuenta != cuentaEntradas:
                    escritor.writerow(diccionarioViejo[cuenta])
                    cuenta = cuenta + 1 
                archivoLibro.close()
                
                
                
               
    
    input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
    return main()
                       
def prestarLibroDeLista(personaActual): 
    
    disponibles =[]
    
    
    
        
    print(f"\n::::::: LISTA DE LIBROS DISPONIBLES PARA PRESTAR :::::::\n\n")
    x = 0
    k = 1
    opcionesValidas=[]
    opcion = 1
            
    
    while (x != len(libros)):
      if (libros[x]['Estado'])== "Disponible":
        disponibles.append(libros[x]['Titulo'])
        opcionesValidas.append(opcion)
           
        print (f"{k} {libros[x]['Titulo']} / {libros[x]['Autor']}")
        opcion = opcion + 1
        k = k+1
      x = x+1 
         
    
    valor = int(input("\nDigita el numero del libro que quieres pedir prestado\n\n---> "))
    
    
    
    if valor not in opcionesValidas:
        print("\nEse libro no esta en la lista, presiona cualquier tecla para ver la lista y elige tu libro\n") 
        input()
        return (prestarLibroDeLista(personaActual))   
    
    
    
    print(f"\n::::::  {disponibles[valor-1]}  :::::::\n")
    
    
    choice = input("\nQuieres pedir prestado ese libro ?\n1- Si\n2- No \n---->")
    if choice =="1":
        tiempoPrestamo=int(input("\nTenemos 3 posibles opciones de tiempo para ti, elige uno\n\n1- 15 Dias\n2- 1 Mes\n3- 45 Dias\n---> "))
        prestarLibroTiempo(tiempoPrestamo,disponibles[valor],personaActual)
     
        
    elif choice =="2":
        return prestarLibroDeLista(personaActual)  
    elif choice  != "1" and choice != "2":
        
        print("\nEsa opcion no es valida")
        return prestarLibroDeLista(personaActual)


def prestarLibro(nombreDeLibroPrestamo,personaActual):
    
        
    
    print(f"::::::: {nombreDeLibroPrestamo} :::::::")
    print("\nDeseas pedir este libro a la Biblioteca ? \n--->")
    tiempoPrestamo=int(input("\nTe gustaria tener este libro por:\n\n1- 15 Dias\n2- 1 Mes\n3- 45 Dias\n---> "))
     
    
    return prestarLibroTiempo(tiempoPrestamo,nombreDeLibroPrestamo,personaActual)
    
 
    
        

def buscandoLibro():
    
    
    indice=1
    titulosTemporales=[] 
    estadosTemporales=[]
    devolucionTemporal=[]
    temporal=[]
    encontrado = 0
    x = 0 
    
    
    
    
    while x < len(libros):
      titulosTemporales.append(libros[x]["Titulo"])
      estadosTemporales.append(libros[x]["Estado"])
      devolucionTemporal.append(libros[x]["Fecha de Devolucion"])
      dueñoActual.append(libros[x]["Dueño Actual"])
      
      x = x+1  
      y= 0
    buscar = input("\nHola, ingresa el nombre del libro o parte del titulo   ----- > ").title()
    
    for x in titulosTemporales:
        if buscar.capitalize() == x:
            encontrado = encontrado + 1
          
       
    
    for x in titulosTemporales: 
        
        
        while y != len(titulosTemporales):
            
            for k in titulosTemporales: 
            
                if  titulosTemporales.index(x) not in temporal and (titulosTemporales[y][0:len(buscar)]) == buscar.title() :
                    temporal.append(titulosTemporales.index(titulosTemporales[y]))
                    encontrado += 1
                    
                y= y +1
                
                
               
        check = x.split() 
        
        if buscar.split() == check and titulosTemporales.index(x) not in temporal:
            encontrado += 1
            temporal.append(titulosTemporales.index(x))
               
          
                
        for k in check: 
            if buscar.split() == k.title() or buscar == k.title() and titulosTemporales.index(x) not in temporal:
                encontrado += 1
                temporal.append(titulosTemporales.index(x))
                    
    if encontrado > 1 and estadosTemporales[temporal[0]] == "Disponible": 
      print("\n::::::::: TENEMOS VARIOS LIBROS CON ESE NOMBRE :::::::\n")
      
     
      
      
      
       
        
      nombreDeLibroPrestamo=titulosTemporales[temporal[0]]
      for x in temporal:
               
         print(f"{indice} - {titulosTemporales[x]}")
         indice = indice + 1   
         encontrado = encontrado - 1 
      eleccion = int(input("\nEscribe el numero del libro que deseas ver de la lista ---> "))
      print ("\n::::::::: ENCONTRE TU LIBRO :::::::\n")
      print (f"\nTitulo: {titulosTemporales[temporal[eleccion-1]]}\nEstado: Este libro se encuentra [ {estadosTemporales[temporal[eleccion-1]]} ]\n" ) 
      
      print("\n   --> Deseas pedir este libro ? <--   \n")
      choice = input("\n1- Si\n2- No\n--->  ")
      respuestasValidas = ["1","2"]
      if choice == "1":
         print("\nMuy bien, porfavor presiona una tecla para registrarte y darte el libro\n")
         nombreDeLibroPrestamo =  titulosTemporales[temporal[eleccion-1]]  
                
         return idenfiticate(nombreDeLibroPrestamo)
      elif choice == "2": 
         print("\nMuy bien, presiona una tecla para volver al Menu Principal\n")
         input()   
         return(main())
      elif choice not in respuestasValidas:
          print("\n  --> opcion invalida <--  \n")
          return buscandoLibro()
          
    
  
    if encontrado > 1 and estadosTemporales[temporal[0]] != "Disponible": 
      print("\n::::::::: TENEMOS VARIOS LIBROS CON ESE NOMBRE :::::::\n")  
      for x in temporal:
         print(f"{encontrado} - {titulosTemporales[x]}")
      
         encontrado = encontrado - 1 
      eleccion = int(input("\nEscribe el numero del libro que deseas ver de la lista ---> "))
      print ("::::::::: ENCONTRE TU LIBRO :::::::")   
      print (f"\nTitulo: {titulosTemporales[temporal[-eleccion]]}\nEstado: Este libro se encuentra [ {estadosTemporales[temporal[0]]} ]\nSu devolucion esta programada para el dia {devolucionTemporal[temporal[0]]} Propietario Actual --> {dueñoActual[temporal[0]]}\n") 
      input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
      return main()
  
       
     
    elif encontrado == 1 and estadosTemporales[temporal[0]] == "Disponible":
        nombreDeLibroPrestamo=titulosTemporales[temporal[0]]
        print ("\n\n::::::::: ENCONTRE TU LIBRO :::::::\n\n")   
        print (f"\nTitulo: {titulosTemporales[temporal[0]]}\nEstado: Este libro se encuentra [ {estadosTemporales[temporal[0]]} ]\n")
        
        print("\n   --> Deseas pedir este libro ? <--   \n")
        choice = input("\n1- Si\n2- No\n--->")
        respuestasValidas = ["1","2"]
        if choice == "1":
            print("\nMuy bien, porfavor presiona una tecla para registrarte y darte el libro\n")
            input()   
            nombreDeLibroPrestamo =  titulosTemporales[temporal[0]]         
            
            
            return idenfiticate(nombreDeLibroPrestamo)
        elif choice == "2": 
            print("\nMuy bien, presiona una tecla para volver al Menu Principal\n")
            input()   
            return(main())
        elif choice not in respuestasValidas:
            print("\n  --> opcion invalida <--  \n")
            return buscandoLibro()
            
    elif encontrado == 1 and estadosTemporales[temporal[0]] != "Disponible":
        
     
        
        print ("::::::::: ENCONTRE TU LIBRO :::::::") 
        print (f"\nTitulo: {titulosTemporales[temporal[0]]}\nEstado: Este libro se encuentra [ {estadosTemporales[temporal[0]]} ]\nSu devolucion esta programada para el dia {devolucionTemporal[temporal[0]]}\nPropietario Actual --> {dueñoActual[temporal[0]]}")
        input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
        return main()
        
    elif encontrado == 0:
     print ("\n::::::::: NO TENEMOS ESE LIBRO EN NUESTRA COLEECION :::::::\n")
     LibroNoEncontrado()
            
           
def librosPrestados():
    
    
        
    print(f"\n::::::: LISTA DE LIBROS QUE SE ENCUENTRAN PRESTADOS  :::::::\n\n")
    x = 0
    k = 0
    
    while (x != len(libros)):
      if (libros[x]['Estado'])== "Prestado":
         
        print (f"\n{k}- {libros[x]['Titulo']} \n   {libros[x]['Autor']} \n   Fecha de Devolucion --->   {libros[x]['Fecha de Devolucion']}\n   Dueño Actual --->  {libros[x]['Dueño Actual']} ")
        k = k+1
      x = x+1
    input("\n<--- Presiona alguna tecla para ver el Menu Principal  ---->\n") 
    return main()
                

def main():    
    
    
    actualizaArchivoPersona()
    actualizarLibros()
    
    
    opcionesValidas =["a","b","c","d","e","f","g","h","0"]
    eleccion = input(""" 
    a - Ver lista de personas
    b - Ordenar lista de personas
    c - Buscar Personas
    d - Agregar Personas a la lista
    e - Ver lista de libros
    f - Buscar libro
    g - Pedir Libro Prestado
    h - Ver prestamo de libros
    i - Ingresar Libro en Wishlist
    0 - Salir
    \n ---> """).lower()
    
    
    if eleccion == "a":
        return verPersonas()
    
    elif eleccion == "b":
        return ordenarLista()
    
    elif eleccion == "c":
        return buscando()
    
    elif eleccion == "d":
        return agregarPersona()
    
    elif eleccion == "e": 
        return verTodosTitulosLibros()
    
    elif eleccion == "f":
        return buscandoLibro()
    
    elif eleccion == "g":
        sinLibro = "ninguno"
        return idenfiticate(sinLibro)
    
    elif eleccion == "h":
        return librosPrestados()
    
    elif eleccion == "i":
        return pedirNuevoLibro()
    
    elif eleccion == "0":
        return("""
              Gracias por usar este programa. 
              
               Kevin Paniagua Sanchez - 2020
   
          """)
    elif eleccion not in opcionesValidas:
        print("\nOpcion invalida, elige una opcion\n") 
        return main()       


print(main())


        
        
        
     
        

        
        
        
    





