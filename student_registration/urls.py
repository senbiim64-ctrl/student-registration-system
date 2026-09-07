from django.contrib import admin
from django.urls import path
from students import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),

    path('students/', views.student_list, name='student_list'),

    path('register/', views.register_student, name='register'),

    path(
        'student/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),

    path(
        'student/<int:student_id>/edit/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'student/<int:student_id>/delete/',
        views.delete_student,
        name='delete_student'
    ),
]