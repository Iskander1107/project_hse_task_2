"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from main_page.views import index, contacts, contact_with_us, olympic_hse, redirect_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('events/', include('events.urls', namespace='events')),
    path('contacts/', contacts, name='contacts'),
    path('contact_with_us/', contact_with_us, name='contact_with_us'),
    path('olympic_hse/', olympic_hse, name='olympic_hse'),
    path('redirect_page/', redirect_page, name='redirect_page')
]
