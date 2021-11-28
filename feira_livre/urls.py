"""feira_livre URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from projeto.views.views_auth import redirect_login
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projeto/', include('projeto.urls')),
    path('', RedirectView.as_view(url='projeto/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/',LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('accounts/trocarSenha', PasswordChangeView.as_view(template_name='registration/password_change_form.html', success_url=reverse_lazy('login'),), name='trocar_senha'),
    path('accounts/senhaTrocada', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='senha_trocada'),
    path('accounts/profile/', redirect_login , name='redirect_login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
