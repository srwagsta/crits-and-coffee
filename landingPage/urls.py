from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.show_landing, name='landing_page'),
]
