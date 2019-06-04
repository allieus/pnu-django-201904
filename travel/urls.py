from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    # travel/ => Post List
    path('', views.post_list, name='post_list'),
    # travel/숫자/ => Post Detail
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
