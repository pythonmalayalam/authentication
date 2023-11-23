from django.urls import path
from . import views

urlpatterns = [

    # path('register/',views.Register_user,name='register'),
    # path('login/',views.loginUser,name='login'),
    # path('logout/',views.logOut,name='logout'),
    # path('home/',views.HomePage,name='home')

    path("register/",views.userRegistration,name='register'),
    path('accounts/login/',views.loginPage,name='login'),
    path('',views.admin_view,name="admin_view"),
    path('user_view/',views.user_view,name='user_view'),
    path('logout/',views.logout_view,name='logout')



]
