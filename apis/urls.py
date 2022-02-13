from django.urls import path
from . import views

urlpatterns = [

        path('', views.home, name ="home"),
        path('login/', views.login_user, name='login'),
        path('logout/', views.logout_user, name='logout'),
        path('register/', views.register_user, name='register'),
        path('edit_profile/',views.edit_profile, name='edit_profile'),
        path('change_password/',views.change_password, name='change_password'),
        path('search_results/',views.search_results, name='search_results'),
        path('tag_article/<int:id_name>/', views.tag_article, name ='tag_article'),
        path('tag_error/', views.tag_article, name = 'tag_error'),
        path('tagged_articles/',views.tagged_articles, name='tagged_articles'),
        ]