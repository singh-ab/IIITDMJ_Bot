from django.urls import path
from .views import all , all2
urlpatterns = [
    path('get/' , all , name='all'),
    path('getp/' , all2 , name='allp'),
]
