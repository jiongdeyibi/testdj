from django.conf.urls import url
from . import views as learn_views

app_name = 'app'
urlpatterns = [
    url(r'^index/', learn_views.index, name='index'),
    url(r'^home/', learn_views.home, name='home'),
    url(r'^save/', learn_views.save, name='save'),
    url(r'^head/', learn_views.head, name='head'),
]