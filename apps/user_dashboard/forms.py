from django import forms
from django.forms.widgets import ClearableFileInput
from apps.company.models import Company
from apps.userauths.models import User


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address', 'slug', 'category', 'status', 'image', ]
