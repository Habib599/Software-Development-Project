
from django.contrib import admin
from django.urls import path
from musician import views
from album.views import create_album

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_musician, name="home"),
    path('create_musician/', views.create_musician, name="create_musician"),
    path('create_album/', create_album, name="create_album"),
    path('edit_musician/<int:pk>/', views.edit_musician, name="edit_musician"),
    path("delete_musician/<int:pk>/", views.delete_musician, name="delete_musician")
]
