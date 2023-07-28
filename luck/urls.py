from django.urls import path
from .views import home, category, about, contact, category_detail,create_category

urlpatterns = [
    path('', home, name='home'),
    path('category/',  category, name='category'),
    path('category/<pk>/', category_detail, name='category_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('create_category/',  create_category, name='create_category'),

]