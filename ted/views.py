from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy    
from .models import Face, Picture
from .forms import FaceForm, PictureForm
from django.views.generic import DetailView, ListView, CreateView

# Create your views here.

class FaceListView(LoginRequiredMixin,ListView):
    template_name = 'ted/face_list.html'
    context_object_name = 'faces'
    login_url = reverse_lazy('login')
    def get_queryset(self):
        return Face.objects.all()

class FaceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ted/face_add.html'
    model = Face
    form_class = FaceForm
    success_url = reverse_lazy('face_list')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)

class PictureListView(LoginRequiredMixin, ListView):
    model = Picture
    template_name = 'ted/picture_list.html'
    context_object_name = 'pictures'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Picture.objects.filter(face__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['face'] = Face.objects.get(pk=self.kwargs['pk'])
        return context

class PictureCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    template_name = 'ted/picture_add.html'
    form_class = PictureForm
    success_url = reverse_lazy('')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        picture = form.save(commit=False)
        picture.face = Face.objects.get(pk=self.kwargs['pk'])
        picture.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('picture_add', kwargs={'pk': self.kwargs['pk']})
