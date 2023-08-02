from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("list/", views.PostListView.as_view(), name="list"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("list/<int:pk>/", views.PostRetrieveView.as_view(), name="detail"),
    path("update/<int:pk>/", views.PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete"),
]
