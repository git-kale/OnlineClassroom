from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course


def home(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/home.html', context)


class CoursesListView(ListView):
    model = Course
    template_name = 'courses/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['-date']


class CoursesDetailView(DetailView):
    model = Course


class CoursesCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CoursesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


class CoursesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


def about(request):
    return render(request, 'courses/about.html', {'title': 'About'})

def homepage(request):
    return render(request,'courses/homepage.html')

def accepted(request):
    return render(request, 'courses/added_to_course.html')