"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        print(request)
        print(user)
        return '/accounts/login'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AccountAdmin.urls')),
    path('person/', include('AccountManagement.urls')),
    # path('user-account/', include('UserManagement.urls')),

    # Two way registration
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # one way registation
    url(r'^accounts/', include('registration.backends.simple.urls')),
            #Add in this url pattern to override the default pattern in accounts.
    # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
]
urlpatterns += staticfiles_urlpatterns()
