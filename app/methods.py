import random

from app.models import Fight


def handle_uploaded_file_character(f):
    with open('Character/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def toFight(characters, battleUniverse):
    characters = list(characters)
    random.shuffle(characters)
    traits = ['strength', "intelligence", 'agility', 'perception', 'endurance']
    while len(characters) != 1:
        nbTrait = random.randint(2, 5)
        traitsUsed = random.sample(traits, nbTrait)
        traitCharacter1 = []
        traitCharacter2 = []
        for trait in traitsUsed:
            traitCharacter1.append(getattr(characters[0], trait))
            traitCharacter2.append(getattr(characters[1], trait))

        avgCharacter1 = sum(traitCharacter1) / len(traitCharacter1)
        avgCharacter2 = sum(traitCharacter2) / len(traitCharacter2)

        if avgCharacter1 > avgCharacter2:
            fight = Fight.objects.create(fighter1=characters[0], fighter2=characters[1],
                                         winner=characters[0], battleUniverse=battleUniverse)
            fight.save()
            characters.remove(characters[1])
            if len(characters) == 2:
                battleUniverse.winner = characters[0]
                battleUniverse.save()
        else:
            fight = Fight.objects.create(fighter1=characters[0], fighter2=characters[1],
                                         winner=characters[1], battleUniverse=battleUniverse)
            fight.save()
            characters.remove(characters[0])
            if len(characters) == 2:
                battleUniverse.winner = characters[1]
                battleUniverse.save()
