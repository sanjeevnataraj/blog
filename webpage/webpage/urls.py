"""webpage URL Configuration

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
from django.contrib import admin
from django.urls import path
from webapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('signup/',views.signupview,name='signup'),

	path('login/',views.user_login,name="Login_page"),
	
	path('logout/',views.user_logout,name="logout"),

    path('share-post/',views.postview,name="share"),

    path('home/',views.homeview,name="home"),

    path('edit-post/<pk>',views.edit_postview,name = 'editpost'),

    path('delete-post/<pk>',views.deletepost,name = 'deletepost'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
