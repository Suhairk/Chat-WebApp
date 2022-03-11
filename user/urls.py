from re import template
from django.urls import URLPattern
from Chat_app.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
   #path('', views.index ),
   path('register/', views.Register, name='register'),
   #path('login/', views.login, name='login'),
   path('login/',auth_view.LoginView.as_view(template_name='userTemplates/login.html'), name='login'),
   path('', auth_view.LogoutView.as_view(template_name='userTemplates/index.html'), name='logout'),


#    path('login/', auth_view.LoginView.as_view(template_name ='/templates/userTemplate/login.html'))

]