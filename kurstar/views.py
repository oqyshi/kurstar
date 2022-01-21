from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Course, Lesson, Passed, CallBacks
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView
from .permissions import LessonFollowerPermissionMixin, CourseFollowerPermissionMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
import os
from django.utils.translation import gettext


class CoursesView(View):
    ''' Main page with courses'''

    def get(self, request):
        context = {'courses': Course.objects.all()}
        return render(request, 'kurstar/mainkz.html', context)


class MyCoursesView(LoginRequiredMixin, View):
    ''' My courses '''

    def get(self, request):
        context = {'courses': self.request.user.courses.all()}
        return render(request, 'kurstar/mycourses.html', context)


class CoursesTestView(View):
    ''' Test page with courses'''

    def get(self, request):
        context = {'courses': Course.objects.all()}
        return render(request, 'kurstar/kz2.html', context)


class CourseDetailView(LoginRequiredMixin, CourseFollowerPermissionMixin, DetailView):
    model = Course
    template_name = 'kurstar/course.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if Passed.objects.filter(user=self.request.user, course=kwargs['object']).first() is None:
            Passed.objects.update_or_create(
                user=self.request.user,
                course=kwargs['object'],
                defaults={'date': timezone.now(), 'lesson_number': 1}
            )
        context['lessons'] = kwargs['object'].lesson_set.order_by('number')
        return context


class CourseLandingView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        return render(request, f'kurstar/landings/{course_id}.html', {'course': course})


class LessonDetailView(LoginRequiredMixin, LessonFollowerPermissionMixin, DetailView):
    model = Lesson
    template_name = 'kurstar/lesson.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['achievement'] = Passed.objects.filter(user=self.request.user, course=kwargs['object'].course).first()
        context['delta'] = timezone.now() >= context['achievement'].date + datetime.timedelta(days=1)
        td = (context['achievement'].date + datetime.timedelta(days=1) - timezone.now()).seconds
        context['left_hours'], context['left_minutes'], context['left_seconds'] = td // 3600, (td // 60) % 60, td % 60
        return context


class PaymentView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'kurstar/payment.html')


class PassedView(View):

    def post(self, request):
        Passed.objects.update_or_create(
            user=request.user,
            course_id=request.POST.get("course"),
            defaults={'date': timezone.now(), 'lesson_number': request.POST.get("lesson_number")}
        )
        return HttpResponseRedirect(reverse('kurstar:course_detail', kwargs={'pk': request.POST.get("course")}))


class CallMeBackView(View):
    def post(self, request):
        send_mail(
            'Новая заявка:',
            f'Имя: {request.POST.get("name")};\nНомер: {request.POST.get("number")};\nE-mail: {request.POST.get("email")};\nКомментарий: {request.POST.get("comment")}',
            'kurstar.help@gmail.com',
            ['kurstar.kz@gmail.com'],
            fail_silently=True,
        )

        CallBacks.objects.create(
            name=request.POST.get("name"),
            phone_number=request.POST.get("number"),
            email=request.POST.get("email"),
            comment=request.POST.get('comment')
        )

        return HttpResponseRedirect(reverse('kurstar:thanks'))


class ThanksView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'kurstar/thanks.html')


class AboutView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'kurstar/about.html')


class LidMagnitCallMeBackView(View):
    def post(self, request):
        send_mail(
            'Новая заявка:',
            f'Имя: {request.POST.get("name")};\nНомер: {request.POST.get("number")};\nE-mail: {request.POST.get("email")};\nКомментарий: {request.POST.get("comment")}',
            'kurstar.help@gmail.com',
            ['kurstar.leads@gmail.com'],
            fail_silently=True,
        )

        CallBacks.objects.create(
            name=request.POST.get("name"),
            phone_number=request.POST.get("number"),
            email=request.POST.get("email"),
            comment=request.POST.get('comment')
        )

        subject, from_email, to = 'Чек-Лист от Курстар', 'kurstar.help@gmail.com', request.POST.get("email")
        text_content = 'Спасибо за доверие!'
        html_content = '<p>Надеемся, что данный<strong> чек-лист</strong> поможет вам в достижении цели!</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_file(f'{os.getcwd()}/static/pdf/mobilografia.pdf')
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponseRedirect(reverse('kurstar:thanks'))


class LidMagnitView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'kurstar/landings/lidmagnit.html')
