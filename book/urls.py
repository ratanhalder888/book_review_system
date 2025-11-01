from django.urls import path
from book import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('home/', views.home_page, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('registration/', views.registration_page, name='registration-page'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/new/', views.book_create, name='book-create'),
    path('book/<int:pk>/edit/', views.book_update, name='book-update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),
    
]
