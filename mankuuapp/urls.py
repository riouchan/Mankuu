from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('mankuu/', views.mankuu_hompepage, name='mankuu_homepage'),
    path('mankuu_detail/', views.manqoo_relations_view, name='mankuu_detail'),
    path('edit_mankuu/<str:pk>', views.edit_mankuu, name='edit_mankuu'),
    path('delete_mankuu/<str:pk>/', views.delete_mankuu, name='delete_mankuu'),
    path('create/', views.create_mankuu_info, name='create_mankuu_info'),
    path('logout/', views.logoutUser, name='logout'),
]
