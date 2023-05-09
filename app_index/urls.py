from django.urls import path
from app_index.views import inicio, login_request, signup_request, logout_request, inicio2, adminpanel, adminpanel2, adminpanel3, userpanel



urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio2/', inicio2, name="inicio2"),
    path('login/', login_request, name="login"),
    path('logout/',  logout_request, name="logout"),
    path('signup/', signup_request, name="signup"),
    path('adminpanel/', adminpanel, name="adminpanel"),
    path('adminpanel2/', adminpanel2, name="adminpanel2"),
    path('adminpanel3/', adminpanel3, name="adminpanel3"),
    path('userpanel/', userpanel, name="userpanel"),
]