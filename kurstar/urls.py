from django.urls import path

from . import views

app_name = 'kurstar'
urlpatterns = [
    path('', views.CoursesView.as_view(), name='index'),
    path('course/landing/<int:course_id>', views.CourseLandingView.as_view(), name='course_landing'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:course_id>/lesson/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('lidmagnit/', views.LidMagnitView.as_view(), name='lidmagnit'),
    path('pass/', views.PassedView.as_view(), name='pass'),
    path('test/', views.CoursesTestView.as_view(), name='test'),
    path('mycourses/', views.MyCoursesView.as_view(), name='mycourses'),
    path('callme/', views.CallMeBackView.as_view(), name='callme'),
    path('lidmagnitcallme/', views.LidMagnitCallMeBackView.as_view(), name='lidmagnitcallme'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),

]
