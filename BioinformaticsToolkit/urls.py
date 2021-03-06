"""BioinformaticsToolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^$', lambda r: redirect('/index/')),
    url(r'^index/', include('index.urls')),
    url(r'^cpgislands/', include('cpgislands.urls')),
    url(r'^koperation/', include('koperation.urls')),
    url(r'^fasta/', include('fasta.urls')),
    url(r'^boxplot/', include('boxplot.urls')),
    url(r'^needlemanwunsch/', include('needlemanwunsch.urls')),
    url(r'^smithwaterman/', include('smithwaterman.urls')),
    url(r'^sensingmatrix/', include('sensingmatrix.urls')),
    url(r'^phylogenetictree/', include('phylogenetictree.urls')),
    url(r'^admin/', admin.site.urls),
]
