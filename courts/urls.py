from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/slots/', views.api_get_slots, name='api_get_slots'),
    path('api/reserve/', views.api_reserve_slot, name='api_reserve_slot'),
    path('api/enroll/', views.api_enroll_class, name='api_enroll_class'),
]
