from django.forms import ModelForm
from landing_page.models import DeployedApp

class NewAppForm(ModelForm):
    class Meta:
        model = DeployedApp
        fields = [
            'name',
            'description',
            'icon',
            'ip',
            'port'
        ]
