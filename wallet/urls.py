from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^signup/$', views.SignUp.as_view(),name='signup'),
    url(r'^add_money/', TemplateView.as_view(template_name='add_money.html'), name='add_money'),
    url(r'^add/', views.add, name='add'),
    url(r'^sub_money/', TemplateView.as_view(template_name='sub_money.html'), name='sub_money'),
    url(r'^subtract/', views.subtract, name='subtract'),


]


