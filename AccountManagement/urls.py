from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.ListPerson, name='ListPerson'),
    path('create/', views.CreatePerson, name='CreatePerson'),
    path('update/<int:id>/', views.UpdatePerson, name='UpdatePerson'),
    path('delete/<int:id>/', views.DeletePerson, name='DeletePersons'),
]
urlpatterns += staticfiles_urlpatterns()
