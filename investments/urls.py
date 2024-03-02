from django.urls import path, include
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.view_investments, name='investments'),
   
]