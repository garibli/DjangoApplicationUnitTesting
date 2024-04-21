## Fuad Garibli Yazılım Testi Ödev-1
## Burada index sayfalarını django sayesinde tarayıcıda doğru bir şekilde görüntülemek için path ayarlamalarını yapıyoruz
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index2', views.index2, name='index2'),
]