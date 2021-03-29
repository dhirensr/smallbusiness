from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ("name", "category", "url", "description")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Business/Website name"}
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "url",
                    "placeholder": "https://www.example.com/",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description of what your "
                    "business does in 100 words",
                }
            ),
        }
