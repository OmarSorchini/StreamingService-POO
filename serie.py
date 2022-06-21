# Eva Denisse Vargas Sosa A01377098
# Omar Rodrigo Sorchini Puente A01749389
class Serie:
    """Clase de tipo Serie. """
    
    def __init__(self, idSerie, nombre):
        """Inicializador de clase Serie que guarda los datos basicos de la misma.

            idSerie = id de la serie(str)
            nombre = nombre de la serie(str)
            duracion = duracion de la serie(int)
            genero = gnero de la serie(str)
            calificacion = calificacion de la serie(float)
            estreno = fecha de estreno(str)"""
        
        self.idSerie = idSerie
        self.nombre = nombre
        self.listaEpisodios = []
    
    @property
    def getidSerie(self):
        """Propiedad de lectura que devuelve el id de la serie."""
        return self.idSerie
    
    @property
    def getNombre(self):
        """Propiedad de lectura que devuelve el nombre de la serie."""
        return self.nombre
    
    
    @property
    def getListaEpisodios(self):
        """Propiedad de lectura que devuelve la lista de episodios de la serie."""
        return self.listaEpisodios
        
    def mostrar_info(self):
        
        """Metodo que permite mostrar la informacion de la serie."""
        
        
        txt = f"Serie: {self.getNombre}"
        return txt

        
    def agregar_episodio(self, episodio):
        """Metodo que permite agregar episodios a la serie"""
        self.listaEpisodios.append(episodio)
        
    
        
