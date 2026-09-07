<<<<<<< HEAD
"""
URL configuration for student_registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]
=======
from django.contrib import admin
from django.urls import path
from students import views


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
# Login
path(
    'login/',
    views.login_view,
    name='login'
),

# Logout
path(
    'logout/',
    views.logout_view,
    name='logout'
),
    # Home
    path(
        '',
        views.home,
        name='home'
    ),

    # Student list
    path(
        'students/',
        views.student_list,
        name='student_list'
    ),

    # Register student
    path(
        'register/',
        views.register_student,
        name='register'
    ),

    # Student detail
    path(
        'student/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),

    # Edit student
    path(
        'student/<int:student_id>/edit/',
        views.edit_student,
        name='edit_student'
    ),

    # Delete student
    path(
        'student/<int:student_id>/delete/',
        views.delete_student,
        name='delete_student'
    ),
]
>>>>>>> 3c1725c870939e679fdd4dd4b049892e95a3f262
