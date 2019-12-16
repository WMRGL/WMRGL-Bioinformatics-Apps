from django.conf import settings
from django.shortcuts import render
from django.views import View

from landing_page.models import DeployedApp


# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}
        deployed_apps = DeployedApp.objects.all()
        return render(request, 'index.html')
