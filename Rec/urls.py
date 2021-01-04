from django.urls import path
from . import views
from django.conf.urls import include

app_name = "Rec"   



urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("question_view", views.question_view, name="question_view")

]