from django.urls import path
from .views import register,login_view,logout_view,csrf,me



urlpatterns = [
    # add the authentication views  
    path("register/",register),
    path("login/",login_view),
    path("logout/",logout_view),
    path("csrf/",csrf),
    path('me/',me)
]