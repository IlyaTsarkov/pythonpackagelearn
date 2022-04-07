from django.forms import ModelForm
from .models import Package


class NewPackage(ModelForm):
    class Meta:
        model = Package
        fields = ['title', 'description', 'url']

