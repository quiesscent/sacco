from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard'),
    path('login', views.login_, name='login'),
    path('register', views.register_, name='register'),
    path('logout', views.logout_, name='logout'),
    path('user/update', views.update_profile, name='update'),
    path('chart_data', views.chart_data, name='chart_data'),
    path('add_dependant',  views.add_dependant, name='add_dependant'),
]
