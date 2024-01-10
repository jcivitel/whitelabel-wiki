from django import forms

from wikibackend.models import WikiPage


class EditorForm(forms.ModelForm):
    class Meta:
        model = WikiPage
        fields = ('content',)
        widgets = {"content": forms.Textarea(attrs={"class": "form-control mb-3", "rows": 25})}
