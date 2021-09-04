"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('profile', views.profile, name="profile"),
    path('afterlogin', views.afterlogin, name="afterlogin"),
    path('logout1', views.logout1, name="logout1"),
    path('mycourses', views.mycourses, name="mycourses"),
    path('order', views.order, name="order"),

    # path('contact/',views.contact,name='contact'),
    # path('about1/',views.about1,name='about1'),
    # path('contact1/',views.contact1,name='contact1'),
    # path('sample',views.sample,name='sample'),
    # path('signup', views.handleSignUp, name="handleSignUp"),
    # path('login', views.handeLogin, name="handleLogin"),
    # path('logout', views.handelLogout, name="handleLogout"),
    # path('report', views.report, name="report"),
    #
    # path('my_complaints', views.my_complaints, name="my_complaints"),


]
