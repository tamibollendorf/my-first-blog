from django.conf.urls import url
from . import views
from .views import post_list
urlpatterns = [url(r'^$', post_list, name= 'post_list')]