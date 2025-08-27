from django.urls import path

from pages.views import eror_404_view, about_view, coming_soon_view, contact_view, faq_view, home_view

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('404/', eror_404_view, name='404'),
    path('about/', about_view, name='about'),
    path('coming-soon/', coming_soon_view, name='coming-soon'),
    path('contact/', contact_view, name='contact'),
    path('faq/', faq_view, name='faq')
]