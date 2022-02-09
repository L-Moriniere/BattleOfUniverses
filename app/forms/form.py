from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Column, Fieldset
from django import forms
from django.forms import Form, ModelForm
from django.utils.safestring import mark_safe

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


class CharacterImageForm(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return mark_safe("<img src='%s' alt='image_character'/><br><h3>%s</h3>" % (obj.image.url, obj.name))


class BattleUniverseForm(ModelForm):
    characters = CharacterImageForm(queryset=Character.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = BattleUniverse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(
                InlineCheckboxes('characters'),
            )
        )
