"""iMagic_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from my_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    #path('course_title', views.add_title),get_all_projects_es
    path('<str:label_name>', views.get_course_titles),
    path('elastic/<str:label_name>', views.get_course_titles_es),
    path('projects/', views.get_all_projects),
    path('projects/elastic/', views.get_all_projects_es),
    path('projects/elastic/<int:project_id>', views.get_project_by_id_es),
    path('projects/<int:proj_id>', views.get_project), 
]
