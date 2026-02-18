from django.urls import path
from . import views

urlpatterns = [
    path('suggest/', views.suggestion_view, name='suggestion_form'),
    path('thanks/', views.thanks_view, name='thanks_page'),
]