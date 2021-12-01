from django import forms
from .models import Team, Profile

class TeamForm(forms.ModelForm):
    def clean(self):
        name = self.cleaned_data['name']
        if not name.istitle():
            raise forms.ValidationError({'name': 'The team name must start with a capital letter'})
        if Team.objects.filter(name=name).exists():
            raise forms.ValidationError({"name": 'This Team already exist'})


class ProfileForm(forms.ModelForm):
    pass



