from django.urls import path
from . import views

urlpatterns = [
    path('', views.Gallery.as_view(), name='index'),
    path('collections/', views.CollectionListView.as_view(), name='collections'),
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),
]