from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:choice>/vote', views.vote, name='vote'),
    path('undo_vote', views.undo_vote, name='undo_vote'),
]
