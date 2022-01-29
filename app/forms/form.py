from django import forms
from django.forms import Form, ModelForm
from app.models import Universe, Character, BattleUniverse


class LoginForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)


class UploadImgUniverseForm(forms.Form):
    model = Universe
    image = forms.ImageField()


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'description', 'strength', 'perception', 'agility', 'intelligence', 'endurance', 'image']

    universe = forms.ModelChoiceField(queryset=Universe.objects.all())


class BattleUniverseForm(ModelForm):
    class Meta:
        model = BattleUniverse
        fields = '__all__'

    characters = forms.ModelMultipleChoiceField(queryset=Character.objects.all(), widget=forms.CheckboxSelectMultiple())
