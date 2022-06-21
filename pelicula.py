# Eva Denisse Vargas Sosa A01377098
# Omar Rodrigo Sorchini Puente A01749389
from video import Video
class Pelicula(Video):
    """Clase de tipo Pelicula. """
    
    def __init__(self,idVideo, nombre, duracion, calificacion,estreno, genero):
        """Inicializador de clase Pelicula con datos heredados y genero"""
        
        super().__init__(idVideo, nombre, duracion, calificacion,estreno)
        
        self.genero = genero
    
    @property
    def getGenero(self):
        """Propiedad de lectura que devuelve el genero. """
        return self.genero
        
    def mostrar_video(self):
        """Metodo que permite mostrar la informacion de la pelicula."""
        
        txt = f"""
Pelicula: {self.getNombre}
Duracion: {self.getDuracion} minutos
Género: {self.getGenero}
Calificacion: {self.getCalificacion}
Fecha de estreno: {self.getEstreno}
"""
        
        return txt
    
#a = Pelicula(44,"Uuw", 45, "amor", "mayo")