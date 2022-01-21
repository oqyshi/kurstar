from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Lesson, Course, Materials, Passed, CallBacks


class LessonAdminForm(forms.ModelForm):
    description = forms.CharField(label='Контент урока', widget=CKEditorUploadingWidget())

    class Meta:
        model = Lesson
        fields = '__all__'


class MaterialsInline(admin.TabularInline):
    model = Materials
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'course', 'title', 'visible')
    list_display_links = ('title',)
    list_filter = ('course__title',)
    search_fields = ('title', 'course__title')
    list_editable = ('visible',)
    inlines = [MaterialsInline]
    save_on_top = True
    form = LessonAdminForm


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image', 'visible')
    list_display_links = ('title',)
    save_on_top = True

    readonly_fields = ("get_image",)
    list_editable = ('visible',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.banner.url} width="200" height="110">')

    get_image.short_description = "Изображение"


@admin.register(CallBacks)
class CallBacksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'date', 'comment', 'called')
    search_fields = ('name',)
    save_on_top = True
    list_editable = ('called',)


@admin.register(Passed)
class PassedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'date')
    list_display_links = ('id',)
    search_fields = ('user__email', 'user__username')
    list_filter = ('course',)
    save_on_top = True


admin.site.register(Materials)

admin.site.site_title = "Панель Администратора KURSTAR"
admin.site.site_header = "Панель Администратора KURSTAR"


# def get_queryset(self, request):
#     qs = super(ArticleModelAdmin, self).get_queryset(request)
#     return qs.filter(author=request.user)