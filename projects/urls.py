from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entries/', views.ProjectListView.as_view(), name='entries'),
]
