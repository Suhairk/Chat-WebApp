from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='user-home'),
    path('<str:group>/', views.group , name='group'),
#checking existance
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
    path('getMessages/<str:group>/', views.getMessages , name="getMessages"),
    
    path('private/<str:sender>/<str:receiver>/', views.private_chat,name="private_chat"),
    path('sendPrivateMsg', views.sendPrivateMsg, name ='sendPrivateMsg'),
    path('getPrivateMessages/<str:sender>/<str:receiver>/', views.getPrivateMessages ,                    
                                                            name="getPrivateMessages"),


]
