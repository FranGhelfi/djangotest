from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),

]

from catalog.views import AboutView

urlpatterns += [
    # url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^about/$', views.AboutView, name='about'),
]

urlpatterns += [
    # url(r'^about/$', views.AboutView.as_view(), name='about'),
    # url(r'^moises-sanchez/$', views.ArtistaView, name='artista'),

    #url(r'^<person_id>/$', views.ArtistaView, name='artista'),
    #url(r'^category/(?P<person_id>[\w-]+)/$', views.ArtistaView, {'person_id': 'person_id'}, name='artista'),
    url(r'^artistas/(?P<person_id>\D+)/$', views.ArtistaView, name="artista"),
]

