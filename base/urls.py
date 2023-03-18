from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('contact', views.contact , name="contact"),
    path('about', views.about , name="about"),
    path('team', views.team , name="team"),
    path('blogs', views.blogs , name="blogs"),
    path('blog/<str:pk>/', views.blog , name="blog"),
    
    path('projects', views.projects , name="projects"),
    path('project/<str:pk>/', views.project , name="project"),
    
    path('donations', views.donations , name="donations"),
    path('donation/<str:pk>/', views.donation , name="donation"),
    
]

