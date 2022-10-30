from django.urls import path, include
from fake_news_detection import views


urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('result/', views.result, name="result"),
    path('news/', views.news, name="news"),
    path('paytm/', views.paytm, name="paytm"),
    path('contact/', views.contact, name="contact"),
    path('satisfaction/', views.satisfaction, name="satisfaction"),
]
