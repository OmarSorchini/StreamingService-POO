# Eva Denisse Vargas Sosa A01377098
# Omar Rodrigo Sorchini Puente A01749389

from video import Video

class Episodio(Video):
    """Clase de tipo Episodio. """
    
    def __init__(self, idVideo, nombreEps, duracion, calificacion, estreno, numEpisodio, temporada, genero):
        """Inicializador de clase con datos basicos y serie correspondiente.

            idVideo = id del episodio(str)
            nombreEps = nombre del episodio(str)
            duracion = duracion del episodio(int)
            calificacion = calificacion del episodio(float)
            estreno = fecha de estreno(str)
            numEpisodio = numero del Episodio(int)
            temporada = temporada a la que pertenece(int)
            
            """
        super().__init__(idVideo, nombreEps, duracion, calificacion,estreno)
        
        self.temporada = temporada
        self.numEpisodio = numEpisodio
        self.genero = genero
    
    @property
    def getTemporada(self):
        """Propiedad de lectura que devuelve la temporada."""
        return self.temporada
    
    @property
    def getNumEpisodio(self):
        """Propiedad de lectura que devuelve el numero del episodio."""
        return self.numEpisodio
    @property
    def getGenero(self):
        """Propiedad de lectura que devuelve el numero del episodio."""
        return self.genero
        
    def mostrar_video(self):
        """Metodo que permite mostrar la informacion del episodio. """
        
        txt = f"""
Nombre: {self.getNombre}
Duracion: {self.getDuracion} minutos
Fecha de estreno: {self.getEstreno}
Calificacion: {self.getCalificacion}
Genero: {self.getGenero}
Temporada: {self.getTemporada}
Numero de episodio: {self.getNumEpisodio}
"""
        
        return txt
    
#a = Episodio(44,"uwu", 45, "trro", "45", 2, 3)