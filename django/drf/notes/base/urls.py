from django.urls import path
from .views import *

urlpatterns = [

    path('list/', NotesListView.as_view()),
    path('create/', NotesCreateView.as_view()),
    path('<int:pk>/', NotesDetailView.as_view()),
    path('<int:pk>/update/', NotesUpdateView.as_view()),





]
