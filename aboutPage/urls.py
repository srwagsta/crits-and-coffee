from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/', views.show_about, name='about_page'),
]
