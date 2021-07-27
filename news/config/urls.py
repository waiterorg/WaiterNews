"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from django.conf.urls import include
from . import settings
from main_account.views import Login, Register, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login' ),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('activate/<uidb64>/<token>)/', activate, name='activate'),
    path('', include('django.contrib.auth.urls')),
    path('', include('news_app.urls')),
    path('comment/', include('comment.urls')),
    path('account/', include('main_account.urls')),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)