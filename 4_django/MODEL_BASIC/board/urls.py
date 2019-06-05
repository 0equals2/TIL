from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new_article),
    path('create/', views.create_article), #board/create/
    # Read
    path('', views.article_list), #/board/
    path('<int:article_id>/', views.article_detail), #board/2/
    # Update
    path('<int:article_id>/edit/',views.edit_article),
    path('<int:article_id>/update/', views.update_article),
    # Delete
    path('<int:article_id>/delete/',views.delete_article), # /board/1/delete/
]
