import random
from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView

from app.forms.form import LoginForm, UploadImgUniverseForm, BattleUniverse, CharacterForm, BattleUniverseForm
from app.methods import toFight
from app.models import Character, BattleUniverse, Universe, CharacterUniverse, BattleUniverseCharacter, Fight


class IndexView(TemplateView):
    template_name = "index.html"


class CharacterListView(ListView):
    template_name = "character_list_view.html"
    model = Character


class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy('character_list')
    template_name = "character_delete.html"


class CharacterDetailView(DetailView):
    template_name = 'character_detail_view.html'
    model = Character

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['universe'] = Universe.objects.filter(
            characteruniverse__character__pk=self.object.pk
        )
        return result


class CharacterCreateView(CreateView):
    template_name = "character_create.html"
    model = Character
    success_url = reverse_lazy('character_list')
    form_class = CharacterForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        strength = form.cleaned_data['strength']
        perception = form.cleaned_data['perception']
        agility = form.cleaned_data['agility']
        intelligence = form.cleaned_data['intelligence']
        endurance = form.cleaned_data['endurance']
        image = form.cleaned_data['image']
        universe = form.cleaned_data['universe']
        character = Character.objects.create(name=name, description=description, strength=strength,
                                             perception=perception, agility=agility, endurance=endurance,
                                             intelligence=intelligence, image=image)
        characterUniverse = CharacterUniverse.objects.create(character=character, universe=universe)
        character.save()
        characterUniverse.save()
        return HttpResponseRedirect('/characters')

    def is_valid(self):
        pass


class CharacterUpdateView(UpdateView):
    template_name = "character_update.html"
    model = Character
    success_url = reverse_lazy('character_list')
    form_class = CharacterForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/characters')

    def is_valid(self):
        pass


class UniverseListView(ListView):
    template_name = "universe_list_view.html"
    model = Universe


class UniverseCreateView(CreateView):
    template_name = "universe_create.html"
    model = Universe
    fields = '__all__'
    success_url = reverse_lazy('universe_list')

    def upload(request):
        if request.method == "POST":
            form = UploadImgUniverseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/universes/')
        else:
            form = UploadImgUniverseForm()
        return render(request, 'universe_list_view.html', {'form': form})


class UniverseUpdateView(UpdateView):
    template_name = "universe_update.html"
    model = Universe
    fields = '__all__'
    success_url = reverse_lazy('universe_list')

    def upload(request):
        if request.method == "POST":
            form = UploadImgUniverseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/universes/')
        else:
            form = UploadImgUniverseForm()
        return render(request, 'universe_list_view.html', {'form': form})


class UniverseDetailView(DetailView):
    template_name = 'universe_detail_view.html'
    model = Universe

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['characters'] = Character.objects.filter(
            characteruniverse__universe__pk=self.object.pk
        )
        return result


class BattleUniverseListView(ListView):
    template_name = "battle_universe_list_view.html"
    model = BattleUniverse


class BattleUniverseDetailView(DetailView):
    template_name = 'battle_universe_detail_view.html'
    model = BattleUniverse

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        print(self.object.pk)
        result['fights'] = Fight.objects.filter(
            battleUniverse__pk=self.object.pk
        )
        return result


class BattleUniverseCreateView(CreateView):
    template_name = "battle_universe_create.html"
    model = BattleUniverse
    success_url = reverse_lazy('battle_universe_list')
    form_class = BattleUniverseForm

    def form_valid(self, form):
        characters = form.cleaned_data['characters']
        name = form.cleaned_data['name']
        battleUniverse = BattleUniverse.objects.create(date=date.today(), nbFighter=len(characters), name=name)
        battleUniverse.save()
        for character in characters:
            character = BattleUniverseCharacter.objects.create(battle_universe=battleUniverse, character=character)
            character.save()

        toFight(characters, battleUniverse)
        return HttpResponseRedirect(reverse('battle_universe_detail', args=(battleUniverse.id,)))

    def is_valid(self):
        pass


class LoginFormView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(self.request, user)
            messages.add_message(
                self.request, messages.INFO,
                f'Hello {user.username}!'
            )
            return super().form_valid(form)
        form.add_error(None, "email / mdp invalide")
        return super().form_invalid(form)

    def form_invalid(self, form):
        pass


class LogoutView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)


class UserCreateView(CreateView):
    template_name = "user_create.html"
    model = User
    success_url = reverse_lazy("index")
    fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email, password=password)
        user.save()
        authenticate(email=email, password=password)
        return super().form_valid(form)
