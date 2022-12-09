from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:equipe>/results', views.results, name='results'),
    path('<int:ligue>/', views.detail, name='detail')
]