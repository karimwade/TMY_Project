from django.urls import path
from tmy_app import views
urlpatterns = [
    path('home',views.create_tmy_parameter,name="index"),
    path('success',views.success,name="success"),
   
]