from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ahmed_drive import views
from django.views.generic.base import RedirectView

urlpatterns = [
# Normal pages
    path('home/', views.HomeView.as_view()),
# Shows Views
#    path('show/', views.ShowListView.as_view()),
#    path('show/<int:pk>', views.ShowDetailView.as_view()),
# Root URL
    path('', RedirectView.as_view(url="home/")), 
]