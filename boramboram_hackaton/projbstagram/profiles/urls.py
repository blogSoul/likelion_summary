from django.urls import path
from . import views

urlpatterns = [
    path('profile/home/', views.profile_home, name="profile_home"),
    path('profile/blog/', views.profile_blog, name="profile_blog"),
    path('profile/comment/', views.profile_comment, name="profile_comment"),
]

