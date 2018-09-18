from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^user$', views.index),
    url(r'(?P<word>\w+)$', views.form),
]