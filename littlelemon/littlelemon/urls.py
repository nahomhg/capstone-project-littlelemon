"""littlelemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    # Frontend where the user interacts
    path('app/',include('frontend.urls')),
    # API endpoints to call.
    path('api/', include('restaurant.urls')),
    # path('api/booking/', include(router.urls)),
    # Authentication endpoints
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
]
