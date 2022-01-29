from django.contrib import admin

# Register your models here.
from app.models import BattleUniverse, Fight, Character, Universe, CharacterUniverse, BattleUniverseCharacter


class CharacterUniverseInlineAdmin(admin.TabularInline):
    model = CharacterUniverse
    extra = 1


class CharacterUniverseAdmin(admin.ModelAdmin):
    inlines = (CharacterUniverseInlineAdmin,)


admin.site.register(Universe, CharacterUniverseAdmin)
admin.site.register(Character)
admin.site.register(Fight)
admin.site.register(BattleUniverse)
admin.site.register(BattleUniverseCharacter)
admin.site.register(CharacterUniverse)
