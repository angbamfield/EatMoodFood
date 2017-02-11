from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^modifyProfile/$', views.modify_profile, name="modify_profile"),
    url(r'main^/$', views.index, name="main")
]
