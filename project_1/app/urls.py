from django.contrib import admin 
from django.urls import path
from .import views

urlpatterns=[
    path('datalists/', views.inputs.as_view()),
    path('lists/', views.department.as_view())
   
]

#http://127.0.0.1:8000/user_list/datalists/   

#http://127.0.0.1:8000/userlist/lists/ 