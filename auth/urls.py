from django.urls import path

from auth.views import login_view, dashboard_view

app_name = 'auth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard')
]