from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path("list/", views.CourseListView.as_view(), name="list"),
    path("create/", views.CourseCreateView.as_view(), name="create"),
    path("list/<int:pk>/", views.CourseRetrieveView.as_view(), name="detail"),
    path("update/<int:pk>/", views.CourseUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.CourseDeleteView.as_view(), name="delete"),
    path("episode/<int:pk>/", views.EpisodeRetrieveView.as_view(), name="episode-detail"),
    path("episode/create/", views.EpisodeCreateView.as_view(), name="episode-create"),
    path("episode/update/<int:pk>/", views.EpisodeUpdateView.as_view(), name="episode-update"),
    path("episode/delete/<int:pk>/", views.EpisodeDeleteView.as_view(), name="episode-delete"),
]