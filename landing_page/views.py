from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView

from landing_page.models import DeployedApp
from landing_page.forms import NewAppForm


# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    form_class = NewAppForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deployed_apps'] = DeployedApp.objects.all()
        return context

    def form_valid(self, form):
        print(form)
        form.save()
        return super().form_valid(form)

class AppDeleteView(DeleteView):
    model = DeployedApp
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        return super().delete(request, *args, **kwargs)
