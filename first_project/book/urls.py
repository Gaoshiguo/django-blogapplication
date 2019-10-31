from django.urls import path
from . import views

urlpatterns =[
    path('',views.book),
    path('detail/<book_id>',views.bookdetail),
    path('author_id/',views.author_id),
]