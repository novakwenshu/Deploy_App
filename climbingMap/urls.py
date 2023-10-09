from django.urls import path
from . import views

#URL Config

urlpatterns = [
   path('', views.index, name='index'),
   path('areas/', views.ClimbingAreaListView.as_view(), 
        name = 'areas'),
   path('area/<int:pk>/', views.ClimbingAreaDetailView.as_view(),
        name='area-detail'),
   path('search_areas', views.search_areas, name="search-areas"),
]

urlpatterns += [path('create/', views.AreaCreate.as_view(), name = 'area-create')]
