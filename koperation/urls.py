from django.conf.urls import url
from . import views

app_name = 'koperation'
urlpatterns = [
    url(r'^$', views.get_page, name='k_operation_page'),
    url(r'^result/$', views.k_operation, name='k_operation'),
]