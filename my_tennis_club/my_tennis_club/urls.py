"""
URL configuration for my_tennis_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings#
#this two import this two this above  writing 'settings' and below 'static' and 
#you have to give link in setting two for media.
from django.conf.urls.static import static#
from my_tennis_club import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about-us/',views.aboutUs,name="about"),
    path('contact-us/',views.contactUs,name="contact"),
    path('service-us/',views.serviceUs,name="service"),
    path('userform/',views.userForm,name ="userForm"),
    path('submitform/',views.submitForm,name = "submitform"),
    path('loginform/',views.login,name="login"),
    path("conection/",views.conection),
    path('calculator-us/',views.calculator,name='calculator'),
    path('NewsData-us/<slug>',views.NewsData,name='NewsData') #how to make dynamic url through slug  and dynamic data with use of for loop
    # path('contact-us/<courseid>',views.contactUs),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # i have to give url like above to set media in the url.py 