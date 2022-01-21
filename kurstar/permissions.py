from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


class LessonFollowerPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return HttpResponseRedirect(reverse('kurstar:payment',))
        return super().dispatch(request, *args, **kwargs)

    def has_permissions(self):
        return self.request.user in self.get_object().course.members.all()


class CourseFollowerPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return HttpResponseRedirect(reverse('kurstar:payment',))
        return super().dispatch(request, *args, **kwargs)

    def has_permissions(self):
        return self.request.user in self.get_object().members.all()
