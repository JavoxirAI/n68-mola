from django.urls import path

from blogs.views import blog_list_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('list/', blog_list_view, name='list'),
    path('detail/', blog_detail_view, name='detail')
]