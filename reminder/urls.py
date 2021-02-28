"""reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView

from apps.todo.views import ListTaskDuetask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('apps.todo.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', ListTaskDuetask.as_view(), name='index'),
    path('common/', include([
        path('ok/', TemplateView.as_view(template_name='succesfully.html'), name='ok'),
        path('404/', TemplateView.as_view(template_name='404.html'), name='404')
    ]
    ), )
]
