from django.db import models


# Datasets de referencia

class Artistas(models.Model):
    nombre_artista = models.CharField(max_length=50, help_text="Nombre del artista")

    def __str__(self):
        return self.nombre_artista

class EstatusProyectos(models.Model):
    estatus_proyectos = models.CharField(max_length=50, help_text="Estatus de proyecto")

    def __str__(self):
        return self.estatus_proyectos

# Datasets de info

class SocialMedia(models.Model):
    marca = models.ForeignKey('Artistas', on_delete=models.CASCADE)
    facebook = models.URLField("Facebook", max_length=128, blank=True)
    instagram = models.URLField("Instagram", max_length=128, blank=True)
    youtube = models.URLField("Youtube", max_length=128, blank=True)
    twitter = models.URLField("Twitter", max_length=128, blank=True)
    spotify = models.URLField("Spotify", max_length=128, blank=True)
    itunes = models.URLField("Itunes", max_length=128, blank=True)
    web = models.URLField("Web", max_length=128, blank=True)
    apple = models.URLField("Apple", max_length=128, blank=True)
    amazon = models.URLField("Amazon", max_length=128, blank=True)
    deezer = models.URLField("Aeezer", max_length=128, blank=True)
    google = models.URLField("Google", max_length=128, blank=True)
    pandora = models.URLField("Pandora", max_length=128, blank=True)

    def __str__(self):
        return str(self.marca)


class Discos(models.Model):
    artista = models.ForeignKey('Artistas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, help_text="Título del disco", blank=True, null=True)
    brief = models.TextField(max_length=300, help_text="Propietario de los links", blank=True, null=True)
    creditos = models.TextField(max_length=500, help_text="Créditos del disco", blank=True, null=True)
    fecha = models.IntegerField(help_text="Año de publicación", blank=True, null=True)
    foto_disco = models.ImageField(upload_to='', blank=True, help_text="Arte de tapa", null=True)
    link_spotify = models.CharField(max_length=300, help_text="Link para escuchar en la web", blank=True, null=True)

    def __str__(self):
        return self.titulo


class Videos(models.Model):
    artista = models.ForeignKey('Artistas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, help_text="Título del disco", blank=True)
    link = models.CharField(max_length=300, help_text="Link al video", blank=True)
    destacado = models.BooleanField(help_text="Destacar el video?", blank=True)

    def __str__(self):
        return self.titulo


class DataArtista(models.Model):
    artista = models.ForeignKey('Artistas', on_delete=models.CASCADE)
    brief = models.TextField(max_length=500, help_text="Título del disco", blank=True)
    bio = models.TextField(max_length=1000, help_text="Link al video", blank=True)
    foto_artista = models.ImageField(upload_to='', default="", blank=True, null=True)
    foto_header = models.ImageField(upload_to='', default="", blank=True, null=True)

    def __str__(self):
        return str(self.artista)

class Fechas(models.Model):
    artista = models.ForeignKey('Artistas', on_delete=models.CASCADE)
    fecha = models.DateField(help_text="Fecha del concierto", blank=True)
    hora = models.TimeField(help_text="Hora del concierto", blank=True)
    ciudad = models.CharField(max_length=50, help_text="Ciudad", blank=True)
    venue_name = models.CharField(max_length=50, help_text="Venue", blank=True)
    venue_direc = models.CharField(max_length=50, help_text="Dirección", blank=True)
    venue_link = models.URLField("Web", max_length=128, blank=True)
    ticket_link = models.URLField("Link a venta de entradas", max_length=128, blank=True)
    ticket_price = models.IntegerField(help_text="Precio de las entradas", blank=True)
    venue_google_maps = models.CharField(max_length=50, help_text="Link de Google maps", blank=True)
    estatus_proyecto = models.ForeignKey('EstatusProyectos', on_delete=models.CASCADE)
    cache_total = models.IntegerField(help_text="Caché total a cobrar", blank=True)
    fee_booking = models.IntegerField(help_text="Fee porcentual", blank=True)
    gastos = models.IntegerField(help_text="Gastos logísticos", blank=True)
    comentarios = models.TextField(max_length=500, help_text="Comentarios", blank=True)
    forma_de_pago = models.TextField(max_length=500, help_text="Forma de pago", blank=True)

    def __str__(self):
        return self.venue_name