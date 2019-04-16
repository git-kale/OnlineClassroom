from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Doubt


def home(request):
    context = {
        'doubts': Doubt.objects.all()
    }
    return render(request, 'doubts/home.html', context)


class DoubtsListView(ListView):
    model = Doubt
    template_name = 'doubts/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'doubts'
    ordering = ['-date']


class DoubtsDetailView(DetailView):
    model = Doubt


class DoubtsCreateView(LoginRequiredMixin, CreateView):
    model = Doubt
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DoubtsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Doubt
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        doubt = self.get_object()
        if self.request.user == doubt.author:
            return True
        return False


class DoubtsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Doubt
    success_url = '/'

    def test_func(self):
        doubt = self.get_object()
        if self.request.user == doubt.author:
            return True
        return False


def about(request):
    return render(request, 'doubts/about.html', {'title': 'About'})