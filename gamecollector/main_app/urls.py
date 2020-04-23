from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('games/', views.games_index, name="index"),
    path('games/<int:game_id>/', views.games_detail, name="detail"),
    path('games/create/', views.GameCreate.as_view(), name="games_create"),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name="games_update"),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name="games_delete"),
    path('consoles/', views.ConsoleList.as_view(), name='console_index'),
    path('consoles/<int:pk>/', views.ConsoleDetail.as_view(), name='console_detail'),
    path('consoles/<int:pk>/update/',
         views.ConsoleUpdate.as_view(), name='console_update'),
    path('consoles/<int:pk>/delete/',
         views.ConsoleDelete.as_view(), name='console_delete'),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='console_create'),
    path('games/<int:game_id>/assoc_console/<int:console_id>/',
         views.assoc_console, name="assoc_console"),
    path('games/<int:game_id>/remove_assoc_console/<int:console_id>/',
         views.remove_assoc_console, name="remove_assoc_console"),
    path('accounts/signup/', views.signup, name="signup"),
]
