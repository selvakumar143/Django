from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('sub-admin/', views.index, name='index'),
    path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()
