# Eva Denisse Vargas Sosa A01377098
# Omar Rodrigo Sorchini Puente A01749389

import csv
from pelicula import Pelicula
from episodio import Episodio 
from serie import Serie

class MiCatalogo:
    """Clase de tipo Catálogo"""
    
    def __init__(self):
        """Inicializador de la clase MiCatalogo con la lista de los
        videos y las series."""
        
        self.listaPeliculas = []
        self.listaSeries = []
        self.listaEpisodios = []
        
    @property
    def getListaPeliculas(self):
        """Propiedad de lectura que devuelve la lista de peliculas."""
        return self.listaPeliculas
    
    @property
    def getListaSeries(self):
        """Propiedad de lectura que devuelve la lista de series."""
        return self.listaSeries
    
    @property
    def getListaEpisodios(self):
        """Propiedad de lectura que devuelve la lista de episodios."""
        return self.listaEpisodios
        
    def cargar_archivo(self):
        """Metodo que permite leer el catalogo de peliculas y series de
        un archivo csv llamado Basepelículas.csv"""
        
        listaPeliculas = []
        listaSeries = []
        
        with open('BasePelículas.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                if row[-1] == '':
                    listaPeliculas.append(row[:-4])
                else:
                    listaSeries.append(row)
                    
        peliculas = []
        series = []
                    
        nombreSeries = []
        for i in listaPeliculas:
            peliculas.append(Pelicula(i[0], i[1], i[2], i[4], i[5], i[3]))
                        
        for i in listaSeries:
            if i[1] not in nombreSeries:
                series.append(Serie(i[0], i[1]))
                nombreSeries.append(i[1])
                            
        peliculas = peliculas[1:]
        series = series[1:]
                    
        for j in series:
            for i in range(len(listaSeries)):
                if j.getNombre == listaSeries[i][1]:
                   series[series.index(j)].agregar_episodio(Episodio(listaSeries[i][9], listaSeries[i][6], listaSeries[i][2], listaSeries[i][4], listaSeries[i][5], listaSeries[i][8],listaSeries[i][7],listaSeries[i][3]))
                        
        episodios = []
        for j in series:
            for k in j.listaEpisodios:
                episodios.append(k)
        
        self.listaPeliculas = peliculas
        self.listaSeries = series
        self.listaEpisodios = episodios
                    
        print("Catalogo cargado con éxito")
        
    def filtrar_calificacion(self, lista, valor):
        """Metodo que permite filtrar e lcatalogo por calificacion mayor
        a cierto valor.
        
            lista = lista de peliculas/series
            valor = valor a filtrar (float)"""
        
        calif = []
        for i in lista:
            if i>valor:
                calif.append(i)
                
        return calif
        
    def conseguir_generos(self, lista):
        """Metodo que permite conseguir los generos del catalogo.

            lista = lista de peliculas/series de donde sacar los generos."""
        
        listGeneros = []
        txt = ""
        for i in lista:
            
            genComp = i.genero
            gen = list(genComp)
            for j in gen:
                
                if "," not in gen:
                    if genComp not in listGeneros:
                        listGeneros.append(genComp)
                        break
                    
                if j != " " and j != ",":
                    txt += j
                if j == ",":
                    if txt not in listGeneros:
                        listGeneros.append(txt)
                    txt = ""
            
            if txt not in listGeneros:
                listGeneros.append(txt)
            txt = ""
        
        return listGeneros
    
    def filtrar_genero(self, lista, genero):
        """Metodo que permite filtrar los generos del tipo de video seleccionado y
        de las series.
        
            lista = lista de peliculas/series
            genero = genero a filtrar (str)"""
        
        listaPelGen = []
        for i in lista:
            if genero in i.genero:
                listaPelGen.append(i)
        
        return listaPelGen
    
        
    def mostrar_videos(self):
        """Metodo de clase que permite mostrar los videos filtrandolos
        como se requiera"""
        
        videos = self.getListaPeliculas + self.getListaEpisodios
        print("Como desea filtrar?")
        print("Por calificacion, genero o ambas?")
                
        try:
            filtro = input().lower()
            if not(filtro == "genero" or filtro == "ambas" or filtro == "calificacion"):
                raise Exception("Debe de ser calificacion, genero o ambas")
        except Exception:
            print("Se debe escoger un valor de los solicitados (calificacion, genero, ambas)")
            print("Aprieta una tecla para continuar")
            input()
        else:
            if filtro == "ambas" or filtro == "calificacion" or filtro == "genero":
                filtroImp = videos    
                        
                if filtro == "calificacion" or filtro == "ambas":
                    
                    try:
                        calificacion = float(input("Arriba de que calificacion quiere los videos?: "))
                        if not (0<calificacion<=10):
                            raise Exception(f"Se debe escoger un valor entre 1 y 10")
                    except Exception:
                        print(f"Se debe escoger un valor entre 1 y 10")
                        print("Aprieta una tecla para continuar")
                        filtro = ""
                        filtroImp = []
                        input()      
                    else:          
                        if filtro == "calificacion":
                            filtroImp = self.filtrar_calificacion(filtroImp, calificacion)
                        else:
                            filtroImp = self.filtrar_calificacion(filtroImp, calificacion)
                                    
                if filtro == "genero" or filtro == "ambas":          
                    listaGeneros = self.conseguir_generos(videos)
                    print("Géneros disponibles")
                    for k in listaGeneros:
                        print(k)
                    try:
                        genero = input("Que genero quiere ver?:\n ")
                        if genero not in listaGeneros:
                            raise Exception
                    except Exception:
                        print("Se debe escoger uno de los generos")
                        print("Aprieta una tecla para continuar")
                        filtro = ""
                        filtroImp = []
                        input()
                    
                    if filtro == "genero":
                        filtroImp = self.filtrar_genero(filtroImp, genero)
                    else:
                        filtroImp =self.filtrar_genero(filtroImp, genero)
                                
                
                for i in filtroImp:
                    if isinstance(i, Serie):
                        for j in i.listaEpisodios:
                            print(j.mostrar_video())
                    else:
                        print(i.mostrar_video())
                    
    def encontrar_titulo(self, lista,nombre):
        """Metodo que permite encontrar un titulo de pelicula/serie en el
        catalogo.
        
            lista = lista de peliculas/series
            nombre = nombre del titulo
            """
        
        for i in lista:
            if(i.nombre == nombre):
            
                return i
        try:
            raise Exception
        except Exception:
            print("No se encontro el titulo")
            print("Presiona una tecla para continuar")
            input()
    def mostrar_episodios(self):
        """Metodo de clase que permite mostrar los episodios de una determinada serie."""
        
        for i in self.getListaSeries:
            print(i.mostrar_info())
        serieNomb = input("Que serie quieres ver?: ")
                    
        serie = self.encontrar_titulo(self.getListaSeries,serieNomb)
        if serie == None:
            return
        for j in serie.getListaEpisodios:
            print(j.mostrar_video())
            
    def mostrar_peliculas(self):
        """Metodo de clase que permite mostrar las peliculas del catalogo
        filtrando las peliculas por una calificacion. """
        
        try:
            calificacion = float(input("Arriba de que calificacion quiere las peliculas?: "))
            if not (0<calificacion<=10):
                raise Exception(f"Se debe escoger un valor entre 1 y 10")
        except Exception:
            print(f"Se debe escoger un valor entre 1 y 10")
            print("Presione una tecla para continuar")
            input()
        
        else:
            filtroCal = self.filtrar_calificacion(self.getListaPeliculas, calificacion)

            print("Películas recomendados")
            for i in filtroCal:
                print(i.mostrar_video())
    
    def calificar_video(self):
        """Metodo de clase que permite calificar un video del catalogo. """
        try:
            tipo = input("Que deseas calificar? (pelicula/episodio): ")
            if not(tipo == "pelicula" or tipo == "episodio"):
                raise Exception
        except Exception:
            print("Se debe de escoger entre pelicula y episodio")
            print("Presiona una tecla para continuar")
            input()
        else:
            
            if tipo.lower() == "pelicula":
                for i in self.getListaPeliculas:
                    print(i.mostrar_video())
                            
            if tipo.lower() == "episodio":
                for j in self.getListaSeries:
                    print("Serie: " + j.nombre, end = "")
                    for k in j.getListaEpisodios:
                        print(k.mostrar_video())
                                
                            
            if tipo.lower() == "pelicula":         
                nombCal = input("Que titulo quieres calificar?: ")
                val = self.encontrar_titulo(self.getListaPeliculas,nombCal)
                if val == None:
                    return
                try:
                    numCalif = float(input("Que puntaje le das del 1 al 10?: "))
                    if not (0.0<numCalif<=10.0):
                        raise Exception(f"El valor {numCalif} debe de ser un valor entre 1 y 10")
                except ValueError:
                    print("Ingresa un valor numerico")
                    print("Presiona una tecla para continuar")
                    input()
                except Exception:
                    print(f"El valor {numCalif} debe de ser un valor entre 1 y 10")
                    print("Presiona una tecla para continuar")
                    input()
                else:
                    for i in range(len(self.getListaPeliculas)):
                        if self.getListaPeliculas[i].nombre == nombCal:
                            self.listaPeliculas[i].calificar(numCalif)
                            
            if tipo.lower() == "episodio":

                nombCal = input("Que titulo quieres calificar?: ")

                serieNomb = ""
                for i in self.getListaSeries:
                    for k in i.listaEpisodios:
                        if nombCal == k.nombre:
                                        
                            serieNomb = i.nombre
                            
                            
                val = self.encontrar_titulo(self.getListaSeries,serieNomb)
                if val == None:
                    return
                
                try:
                    numCalif = float(input("Que puntaje le das del 1 al 10?: "))
                    if not (0.0<numCalif<=10.0):
                        raise Exception(f"El valor debe de ser un valor entre 1 y 10")
                    
                except ValueError:
                    print("Ingrese un valor numerico")
                    print("Presione una tecla para continuar")
                    input()
                except Exception:
                    print(f"El valor debe de ser un valor entre 1 y 10")
                    print("Presiona una tecla para continuar")
                    input()
                else:
                            
                        #titulo = self.encontrar_titulo(lista, numCalif)
                        
                    for i in range(len(self.getListaSeries)):
                        for j in self.getListaSeries[i].listaEpisodios:
                            if j.nombre == nombCal:
                                self.listaSeries[i].listaEpisodios[self.listaSeries[i].listaEpisodios.index(j)].calificar(numCalif)
    def start(self):
        """Inicio del loop principal.

        Crea un menu interactivo donde puedes escoger entre ver los videos
        , las series, las peliculas y permite calificar un titulo.
        Permite salir del sevicio de streaming además de que te permite cargar
        el catalogo."""
        
        ins = 0
        print(" Bienvenido a Ome Video")
        while ins != 6:
            
            print("""
        Escriba una de las siguientes numeros:
            1 - Cargar catalogo
            2 - Mostrar videos
            3 - Mostrar episodios de una serie
            4 - Mostrar peliculas
            5.- Calificar video
            6.- Salir
            
    """)
            try:
                ins = int(input("Qué es lo que desea ver a continuación: \n"))
                if not (0<ins<=6):
                    raise Exception(f"Se debe escoger un valor entre 1 y 6")
            except ValueError:
                print("Ingresa un valor numerico")
                print("Aprieta una tecla para continuar")
                input()
            except Exception:
                print("Se debe escoger un valor entre 1 y 6")
                print("Aprieta una tecla para continuar")
                input()
            else:
                print(f"La opcion fue {ins}")
                if ins == 1:
                    self.cargar_archivo()
                if ins == 2:
                    self.mostrar_videos()
                if ins == 3:
                    self.mostrar_episodios()
                if ins == 4:
                    self.mostrar_peliculas()
                if ins == 5:
                    self.calificar_video()

if __name__ == "__main__":
    streaming = MiCatalogo()
    streaming.start()
    