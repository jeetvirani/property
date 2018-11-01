"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from property.authentication.views import login, forgot_password, \
    reset_password, provide_access, signup

urlpatterns = [
    path('login/', login.Login.as_view(), name='login'),
    path('forgot/', forgot_password.ForgotPassword.as_view(), name='forgot'),
    path('reset/<token>/', reset_password.ResetPassword.as_view(), name='reset'),
    path('signup/<token>/', signup.SignUp.as_view(), name='reset'),
    path('apps/', provide_access.ProvideAccess.as_view(), name='provide_apps')
]
