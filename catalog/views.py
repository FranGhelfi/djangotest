from django.shortcuts import render



# Create your views here.

from .models import SocialMedia, Videos, Discos, DataArtista, Artistas


def index(request):
    variable = SocialMedia.objects.all()
    artistas = Artistas.objects.all()
    return render(request, 'index.html', {
        'artistas': artistas,
        'variable': variable})


def AboutView(request):
    variable = SocialMedia.objects.all()
    return render(request, 'index.html', {'variable': variable})


def ArtistaView(request, person_id):
    variable = SocialMedia.objects.all()
    videos_artista = Videos.objects.all()
    discos_artista = Discos.objects.all()
    data_artista = DataArtista.objects.all()
    artistas = Artistas.objects.all()
    objetivo = person_id

    return render(request, 'catalog/artista.html', {
        'videos_artista': videos_artista,
        'discos_artista': discos_artista,
        'data_artista': data_artista,
        'artistas': artistas,
        'objetivo': objetivo,
        'variable': variable})


