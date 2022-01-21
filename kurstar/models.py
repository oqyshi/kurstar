from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Course(models.Model):
    title = models.CharField('Название курса', max_length=200)
    description = models.TextField('Описание курса', blank=True)
    banner = models.ImageField('Изображение для блока', upload_to='courses_banners/')
    youtube_link_id = models.SlugField('id от видео', max_length=20, blank=True)
    members = models.ManyToManyField(User, related_name='courses', blank=True)
    visible = models.BooleanField('Отображаеться', default=True)
    language = models.CharField('Язык', max_length=20, default='kk')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курстар'

    def get_absolute_url(self):
        return reverse('kurstar:course_landing', args=(self.id,))


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField('Название урока', max_length=200)
    number = models.IntegerField('Номер урока', default=0)
    description = models.TextField("Описание", default='', blank=True)
    youtube_link_id = models.SlugField('id от видео', max_length=20, blank=True)
    visible = models.BooleanField('Отображаеться', default=True)

    def __str__(self):
        return f'{self.number}\t{self.title}'

    class Meta:
        verbose_name = 'Сабақ'
        verbose_name_plural = 'Сабақтар'


class Materials(models.Model):
    course = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField('Наименование файла', max_length=200)
    file = models.FileField(null=True, upload_to='lesson_materials/')
    visible = models.BooleanField('Отображаеться', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалдар'


class Passed(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата', auto_now=True)
    lesson_number = models.IntegerField('Номер урока', default=0)

    def __str__(self):
        return f'{self.date} {self.user} {self.course}'

    class Meta:
        verbose_name = 'Прохождение'
        verbose_name_plural = 'Прохождения'


class CallBacks(models.Model):
    name = models.CharField('ФИО', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=200)
    email = models.CharField('e-mail', max_length=200)
    date = models.DateTimeField('Дата', auto_now=True)
    comment = models.CharField('Комментарий', max_length=500, default='Клиент не оставил коментарий')
    called = models.BooleanField('Обработано', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заявка на обратную связь'
        verbose_name_plural = 'Заявки на обратную связь'
