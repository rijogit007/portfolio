"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from portfolio.views import PortfolioListView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView, UserRegisterView,UserLoginView,Viewportfolio
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view', PortfolioListView.as_view(), name='view_portfolio'),
    path('login', UserLoginView.as_view(), name='login'),
    path('create', PortfolioCreateView.as_view(), name='create_portfolio'),
    path('edit/<int:pk>', PortfolioUpdateView.as_view(), name='edit_portfolio'),
    path('delete/<int:id>', PortfolioDeleteView.as_view(), name='delete_portfolio'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('view/<int:id>', Viewportfolio.as_view(), name='viewp'),
    path('', views.HomeView.as_view(), name='home'),
    path('home2',views.Home2.as_view(),name='home2'),
    path('logout',views.Logout.as_view(),name='logout')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
