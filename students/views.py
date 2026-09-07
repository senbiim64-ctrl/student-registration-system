from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, School


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(
                request,
                'Username or password is incorrect!'
            )

    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')


def student_list(request):
    # User kanaaf school isaa barbaadi
    school = get_object_or_404(
        School,
        user=request.user
    )

    search = request.GET.get('search', '').strip()

    # School user kanaa qofa
    students = Student.objects.filter(
        school=school
    ).order_by('-registration_date')

    if search:
        students = students.filter(
            first_name__icontains=search
        ) | students.filter(
            last_name__icontains=search
        ) | students.filter(
            email__icontains=search
        ) | students.filter(
            grade__icontains=search
        )

    return render(request, 'student_list.html', {
        'students': students,
        'search': search,
        'school': school
    })


@login_required
def register_student(request):
    # School account kanaa
    school = get_object_or_404(
        School,
        user=request.user
    )

    if request.method == 'POST':
        try:
            first_name = request.POST.get(
                'first_name', ''
            ).strip()

            last_name = request.POST.get(
                'last_name', ''
            ).strip()

            email = request.POST.get(
                'email', ''
            ).strip()

            grade = request.POST.get(
                'grade', ''
            ).strip()

            dob = request.POST.get(
                'dob', ''
            ).strip()

            parent_contact = request.POST.get(
                'parent_contact', ''
            ).strip()

            address = request.POST.get(
                'address', ''
            ).strip()

            if not all([
                first_name,
                last_name,
                email,
                grade,
                dob
            ]):
                messages.error(
                    request,
                    "All required fields must be filled!"
                )
                return render(
                    request,
                    'register.html'
                )

            try:
                grade_number = int(grade)
            except ValueError:
                messages.error(
                    request,
                    "Grade must be a number!"
                )
                return render(
                    request,
                    'register.html'
                )

            if grade_number < 1 or grade_number > 12:
                messages.error(
                    request,
                    "Grade must be between 1 and 12!"
                )
                return render(
                    request,
                    'register.html'
                )

            if Student.objects.filter(
                email=email
            ).exists():
                messages.error(
                    request,
                    "A student with this email is already registered!"
                )
                return render(
                    request,
                    'register.html'
                )

            # Student school account kanaatti ofumaan ramada
            student = Student.objects.create(
                school=school,
                first_name=first_name,
                last_name=last_name,
                email=email,
                grade=grade_number,
                date_of_birth=dob,
                parent_contact=parent_contact,
                address=address
            )

            messages.success(
                request,
                f"Student {student.full_name()} registered successfully!"
            )

            return redirect('student_list')

        except Exception as e:
            messages.error(
                request,
                f"Error registering student: {e}"
            )

    return render(request, 'register.html', {
        'school': school
    })


@login_required
def student_detail(request, student_id):
    # Student school account kanaa qofa irraa
    school = get_object_or_404(
        School,
        user=request.user
    )

    student = get_object_or_404(
        Student,
        id=student_id,
        school=school
    )

    return render(request, 'student_detail.html', {
        'student': student,
        'school': school
    })


@login_required
def delete_student(request, student_id):
    school = get_object_or_404(
        School,
        user=request.user
    )

    student = get_object_or_404(
        Student,
        id=student_id,
        school=school
    )

    if request.method == 'POST':
        student_name = student.full_name()
        student.delete()

        messages.success(
            request,
            f"Student {student_name} deleted successfully!"
        )

        return redirect('student_list')

    return render(
        request,
        'student_confirm_delete.html',
        {
            'student': student,
            'school': school
        }
    )


@login_required
def edit_student(request, student_id):
    school = get_object_or_404(
        School,
        user=request.user
    )

    student = get_object_or_404(
        Student,
        id=student_id,
        school=school
    )

    if request.method == 'POST':
        try:
            first_name = request.POST.get(
                'first_name', ''
            ).strip()

            last_name = request.POST.get(
                'last_name', ''
            ).strip()

            email = request.POST.get(
                'email', ''
            ).strip()

            grade = request.POST.get(
                'grade', ''
            ).strip()

            dob = request.POST.get(
                'dob', ''
            ).strip()

            parent_contact = request.POST.get(
                'parent_contact', ''
            ).strip()

            address = request.POST.get(
                'address', ''
            ).strip()

            if not all([
                first_name,
                last_name,
                email,
                grade,
                dob
            ]):
                messages.error(
                    request,
                    "All required fields must be filled!"
                )

                return render(
                    request,
                    'edit_student.html',
                    {
                        'student': student
                    }
                )

            try:
                grade_number = int(grade)
            except ValueError:
                messages.error(
                    request,
                    "Grade must be a number!"
                )

                return render(
                    request,
                    'edit_student.html',
                    {
                        'student': student
                    }
                )

            if grade_number < 1 or grade_number > 12:
                messages.error(
                    request,
                    "Grade must be between 1 and 12!"
                )

                return render(
                    request,
                    'edit_student.html',
                    {
                        'student': student
                    }
                )

            if Student.objects.filter(
                email=email
            ).exclude(
                id=student.id
            ).exists():

                messages.error(
                    request,
                    "Another student is already using this email!"
                )

                return render(
                    request,
                    'edit_student.html',
                    {
                        'student': student
                    }
                )

            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.grade = grade_number
            student.date_of_birth = dob
            student.parent_contact = parent_contact
            student.address = address

            student.save()

            messages.success(
                request,
                f"Student {student.full_name()} updated successfully!"
            )

            return redirect(
                'student_detail',
                student_id=student.id
            )

        except Exception as e:
            messages.error(
                request,
                f"Error updating student: {e}"
            )

    return render(
        request,
        'edit_student.html',
        {
            'student': student,
            'school': school
        }
    )