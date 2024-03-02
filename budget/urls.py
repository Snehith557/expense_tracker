from django.urls import path, include
from . import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.set_budget, name='budget'),
    path('/previous_budget', views.previous_budget, name='previous_budget'),
    path('/submit-budget',views.submit_budget)
    # path(include())
]