from django.urls import path
from . import views

urlpatterns =[
    path('',views.movie),
    path('detail/<movie_id>',views.moviedetail),
    path('author_id/',views.author_id),
]