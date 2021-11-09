from django.urls import path
from .views import user_create_view, user_login_view, user_logout_view


urlpatterns = [
    path('create/', user_create_view, name='user-create'),
    path('login/', user_login_view, name='user-login'),
    path('logout/', user_logout_view, name='user-logout'),
]