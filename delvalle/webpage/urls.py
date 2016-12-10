from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^curriculum/$', CV.as_view(), name='cv'),
    url(r'^de-interes/$', Interes.as_view(), name='deinteres'),
    url(r'^galeria/$', Galeria.as_view(), name='galeria'),
    url(r'^contacto/$', Contacto.as_view(), name='contacto'),
]
