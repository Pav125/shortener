from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/',views.contact_view,name='contact'),
    path('<str:slug>/', views.redirect_short_url, name = 'redirect_short_url'),
]