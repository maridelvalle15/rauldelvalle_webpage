from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]
