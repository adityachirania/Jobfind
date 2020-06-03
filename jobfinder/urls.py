from django.urls import path
from . import views


app_name = 'jobfinder'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("home/", views.home, name="home"),
    # path("home/addjob/",views.add_job, name="add_job")
]