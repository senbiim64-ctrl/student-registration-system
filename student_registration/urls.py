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