from django import forms

from .models import Customer, Task


class InfoForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['description', 'contact_method']


class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'amount', 'directions']
        widgets = {
            'directions': forms.CheckboxSelectMultiple
        }

