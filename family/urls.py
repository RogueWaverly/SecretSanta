from django.urls import path
from family import views

urlpatterns = [
  path('', views.OpenPools, name='Display Open Pools'),
  path('<int:member_id>/', views.EditMember, name='Editing Member'),
]
