# birthday/urls.py
from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path(
        '<int:pk>/comment/', views.CongratulationCreateView.as_view(),
        name='add_comment'
    ),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
]