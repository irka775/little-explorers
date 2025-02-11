from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new/', views.review_create, name='review_create'),
    path('<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('<int:review_id>/delete/', views.review_delete, name='review_delete'),
]
