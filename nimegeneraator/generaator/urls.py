from django.urls import path
from .views import generate_name, delete_all_names, toggle_favorite, download_favorites, download_favorites_csv

urlpatterns = [
    path('', generate_name, name='generate_name'),
    path('delete_all/', delete_all_names, name='delete_all_names'),
    path('toggle_favorite/<int:name_id>/', toggle_favorite, name='toggle_favorite'),
    path('download_favorites/', download_favorites, name='download_favorites'),
    path('download_favorites_csv/', download_favorites_csv, name='download_favorites_csv'),
]
