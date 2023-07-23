from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_poem", views.post_poem, name="post_poem"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path('poem/<int:poem_id>', views.poem_page, name="poem_page"),
    path("like_poem/<int:poem_id>", views.like_poem, name="like_poem"),
    path("unlike_poem/<int:poem_id>", views.unlike_poem, name="unlike_poem"),
    path("delete_poem/<int:poem_id>", views.delete_poem, name="delete_poem"),
    path("liked_poems", views.liked_poems, name="liked_poems"),
    path('poets', views.poets, name="poets"),
]