"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

urlpatterns = [
    # https://stackoverflow.com/questions/23939670/serving-static-files-from-root-of-django-development-server
    # https://stackoverflow.com/questions/27065510/how-to-serve-static-files-with-django-that-has-hardcoded-relative-paths-on-herok/40525157#40525157
    # / routes to index.html
    # url(r'^$', serve,
    #     kwargs={'path': 'index.html'}),

    # static files (*.css, *.js, *.jpg etc.) served on /
    url(r'^(?!/static/.*)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s')),
    path('admin/', admin.site.urls),
    # path('catalog/', include('catalog.urls')),
    # path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', include('users.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
