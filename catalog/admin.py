from django.contrib import admin
from .models import SocialMedia, Artistas, Discos, Videos, DataArtista, Fechas, EstatusProyectos


admin.site.register(Artistas)

class Artistas(admin.ModelAdmin):
    list_display = 'nombre_artista'
    fields = ['nombre_artista']


admin.site.register(EstatusProyectos)

class EstatusProyectos(admin.ModelAdmin):
    list_display = 'estatus_proyectos'
    fields = ['estatus_proyectos']




class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'facebook', 'instagram', 'youtube', 'twitter')
    fields = ['marca', 'facebook', 'instagram', 'youtube', 'twitter', 'spotify', 'itunes', 'web',
              'apple', 'amazon', 'deezer', 'pandora', 'google']

admin.site.register(SocialMedia, SocialMediaAdmin)


class DiscosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'fecha', 'foto_disco')
    list_filter = ('artista', 'fecha')
    fields = [('artista', 'titulo'), ('brief', 'creditos'), ('fecha', "link_spotify"), 'foto_disco']

admin.site.register(Discos, DiscosAdmin)


class VideosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'destacado')
    list_filter = ('artista', 'destacado')
    fields = ['artista', ('titulo', 'destacado'),'link']

admin.site.register(Videos, VideosAdmin)


class DataArtistaAdmin(admin.ModelAdmin):
    list_display = ('artista', 'foto_artista')
    fields = ['artista', ('brief', 'bio'), 'foto_artista', 'foto_header']

admin.site.register(DataArtista, DataArtistaAdmin)


class FechasAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'artista', 'fecha', 'ciudad',
                    'estatus_proyecto', 'cache_total')
    list_filter = ('estatus_proyecto', 'artista', 'ciudad', 'fecha')
    fields = [('artista', 'venue_name', 'fecha', 'hora'), ('ciudad', 'venue_direc'), ('venue_link', 'ticket_link'),
                    'ticket_price', 'venue_google_maps', ('estatus_proyecto', 'cache_total',
                    'fee_booking', 'gastos'), ('comentarios', 'forma_de_pago')]

admin.site.register(Fechas, FechasAdmin)





