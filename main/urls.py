from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_, name='login'),
    path('register', views.register_, name='register'),
    path('user/update', views.update_profile, name='update'),
    path('add_dependant',  views.add_dependant, name='add_dependant')
]
