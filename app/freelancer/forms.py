from django import forms

from .models import Freelancer


class InfoForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['experience', 'description', 'directions', 'contact_info']
        widgets = {
            'directions': forms.CheckboxSelectMultiple
        }
