from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import HiddenInput

from todo.models import Todo


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'conclusion_date', 'edit_date', 'delete_date', 'create_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control', 'max_length': 200}),
            'description': forms.Textarea(attrs={'class': 'form_control', 'max_length': 500}),
            'status': forms.CheckboxInput(attrs={'class': 'form_control'}),
            'conclusion_date': forms.DateTimeInput(attrs={'class': 'form_control'}),
            'edit_date': forms.DateTimeInput(attrs={'class': 'form_control'}),
            'delete_date': forms.DateTimeInput(attrs={'class': 'form_control'}),
            'create_date': forms.DateTimeInput(attrs={'class': 'form_control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
        self.fields['conclusion_date'].widget = HiddenInput()
        self.fields['edit_date'].widget = HiddenInput()
        self.fields['delete_date'].widget = HiddenInput()
        self.fields['create_date'].widget = HiddenInput()
