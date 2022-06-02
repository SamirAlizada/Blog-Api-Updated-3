from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BogListCreateApiView.as_view()),
    path('blogs/<int:pk>', views.BlogDetailApiView.as_view()),

    path('users/', views.UserListCreateApiView.as_view()),
    path('users/<int:pk>', views.UserDetailApiView.as_view(), name='user_detail'),
    path('me/', views.profile),
    path('login/', views.login),

    path('author-point/', views.AuthorPointListCreateApiView.as_view()),
    path('author-point/<int:pk>', views.AuthorPointDetailApiView.as_view()),
]