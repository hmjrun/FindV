from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signature/',views.wx_checkSignature,name='signature'),

]
