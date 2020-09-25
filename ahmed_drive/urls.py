from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ahmed_drive import views
from django.views.generic.base import RedirectView

urlpatterns = [
# Basic pages
    path('home/', views.HomeView.as_view()),
# Folder Model Pages
    path('folder/create/', views.FolderCreate.as_view(success_url="/ahmed_drive/folder")),
    path('folder/', views.FolderListView.as_view()),
    path('folder/<int:pk>', views.FolderDetailView.as_view()),
# Root URL
    path('', RedirectView.as_view(url="home/")), 
]