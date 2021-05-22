from django.urls import path
from . import views

urlpatterns = [
    path('', views.Gallery.as_view(), name='index'),
    path('viewer/<int:pk>/', views.viewer, name='viewer'),
    path('collection-preview/<int:pk>/', views.collection_preview, name='collection-preview'),
    path('collections/', views.CollectionListView.as_view(), name='collections'),
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),
    path('archive/<int:year>/', views.ArchiveYear.as_view(), name='archive-year'),
    path('archive/<int:year>/<str:month>/', views.ArchiveMonth.as_view(), name='archive-month'),
]