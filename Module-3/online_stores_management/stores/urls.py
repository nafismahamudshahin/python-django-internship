from django.urls import path
from stores.views import home,about,contact
urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
]