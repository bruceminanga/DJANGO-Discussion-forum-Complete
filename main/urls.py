from django.urls import path
from django.conf.urls import include
from .views import search
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('support/', views.supportView, name='support'),
    path('work/', views.work, name='work'),
    path('question/', views.question, name='question'),
    path('post/', views.post, name='post'),
    path('preview/', views.preview, name='preview'),
    path('preview2/', views.preview2, name='preview2'),
    path('post_details/<int:pk>', views.post_details, name='post_details'),

    path('signup/', views.signup, name='signup'),
    path('post-remove/<int:pk>', views.post_remove, name='post_remove'),
    path('post-edit/<int:pk>', views.post_edit, name='post_edit'),
    path('results/', views.search, name='search'),







]
