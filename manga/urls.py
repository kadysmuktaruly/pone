from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='manga/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('manga/<int:manga_id>/', views.manga_detail, name='manga_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]
