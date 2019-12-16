from django import forms
from landing_page.models import DeployedApp


class NewAppForm(forms.ModelForm):
    class Meta:
        model = DeployedApp
        fields = [
            'name',
            'description',
            'icon',
            'ip',
            'port'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'The name of the application.'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 1,
                    'placeholder': 'A brief description of the application for users.'
                }
            ),
            'icon': forms.TextInput(
                attrs={
                    'placeholder': 'The FomanticUI v2.8 icon identifier for the app icon.'
                }
            ),
            'ip': forms.TextInput(
                attrs={
                    'placeholder': 'The IP of the VM hosting the app.'
                }
            ),
            'port': forms.TextInput(
                attrs={
                    'placeholder': 'The port which is listening for requests for the app.'
                }
            ),
        }
        labels = {
            'ip': 'VM Host IP',
            'icon': '* FomanticUI 2.8 Icon'
        }

    def as_div(self):
        return self._html_output(
            normal_row='<div class="field" %(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )
