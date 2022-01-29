from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import F


class Universe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Universe', null=True)

    def __str__(self):
        return f"{self.name}" or "? (no title)"


class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    strength = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    perception = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    agility = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    intelligence = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    endurance = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    image = models.ImageField(upload_to="Character")
    nbVictory = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}" or "? (no title)"


class CharacterUniverse(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name} - {self.universe.name}" or "? (no title)"


class BattleUniverse(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    nbFighter = models.IntegerField(default=0, blank=True, null=True)
    winner = models.ForeignKey(Character, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}" or "? (no title)"


class BattleUniverseCharacter(models.Model):
    battle_universe = models.ForeignKey(BattleUniverse, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.battle_universe.id} - {self.character.name}" or "? (no title)"


class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    mail = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mail}" or "? (no title)"


class Fight(models.Model):
    fighter1 = models.ForeignKey(Character, related_name='fighter1', on_delete=models.CASCADE)
    fighter2 = models.ForeignKey(Character, related_name='fighter2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Character, related_name='winner', on_delete=models.CASCADE, null=True)
    battleUniverse = models.ForeignKey(BattleUniverse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.fighter1} vs {self.fighter2} -> {self.winner}" or "? (no title)"


