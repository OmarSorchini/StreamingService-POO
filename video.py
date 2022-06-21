# Eva Denisse Vargas Sosa A01377098
# Omar Rodrigo Sorchini Puente A01749389

from abc import ABC, abstractmethod

class Video(ABC):
    """Clase abstracta de tipo Video. """
    def __init__(self, idVideo, nombre, duracion, calificacion,estreno):
        """Inicializador de clase Video.
            idVideo = id del video(str)
            nombre = nombre del video(str)
            duracion = duracion del video(int)
            calificacion = calificacion del video(float)
            estreno = fecha de estreno(str)
            """
        self.idVideo = idVideo
        self.nombre = nombre
        self.duracion = duracion
        self.estreno = estreno
        self.calificacion = calificacion
    
    @abstractmethod
    def mostrar_video(self):
        """Metodo abstracto que mostrará la informacion del video. """
    @property
    def getidVideo(self):
        """Propiedad de lectura que devuelve el id del video."""
        return self.idVideo
    
    @property
    def getNombre(self):
        """Propiedad de lectura que devuelve el nombre del video."""
        return self.nombre
    
    @property
    def getDuracion(self):
        """Propiedad de lectura que devuelve la duracion del video."""
        return self.duracion
    
    @property
    def getEstreno(self):
        """Propiedad de lectura que devuelve el estreno del video."""
        return self.estreno
    
    @property
    def getCalificacion(self):
        """Propiedad de lectura que devuelve la calificacion del video."""
        return self.calificacion
    
    def calificar(self, valor):
        """Metodo que permite calificar un video sobreecribiendolo.

            valor = nueva calificacion(float)"""
        self.calificacion = valor
        print("Su calificacion ha sido subida con éxito")
    
    def __gt__ (self, valor):
        """Metdo que permite determinar si la calificacion del video es mayor a
            un dado valor.
            
            valor = calificacion a comparar"""
        
        if float(self.calificacion) > valor:

            return True
        else:
            return False
        
        pass 