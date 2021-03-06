"""BattleOfUniverses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import IndexView, CharacterListView, CharacterCreateView, UniverseListView, UniverseCreateView, \
    CharacterDetailView, LoginFormView, BattleUniverseListView, BattleUniverseCreateView, BattleUniverseDetailView, \
    UniverseDetailView, UserCreateView, LogoutView, CharacterUpdateView, UniverseUpdateView, CharacterDeleteView

urlpatterns = [

]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('login', LoginFormView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', UserCreateView.as_view(), name="register"),
    path('', IndexView.as_view(), name="index"),
    path('characters', CharacterListView.as_view(), name="character_list"),
    path('character/new', CharacterCreateView.as_view(), name="character_new"),
    path('character/<int:pk>', CharacterDetailView.as_view(), name="character_detail"),
    path('character/<int:pk>/delete', CharacterDeleteView.as_view(), name="character_delete"),
    path('character/edit/<int:pk>', CharacterUpdateView.as_view(), name="character_edit"),
    path('universes', UniverseListView.as_view(), name="universe_list"),
    path('universe/new', UniverseCreateView.as_view(), name="universe_new"),
    path('universe/<int:pk>', UniverseDetailView.as_view(), name="universe_detail"),
    path('universe/edit/<int:pk>', UniverseUpdateView.as_view(), name="universe_edit"),
    path('battleUniverses', BattleUniverseListView.as_view(), name="battle_universe_list"),
    path('battleUniverse/new', BattleUniverseCreateView.as_view(), name="battle_universe_new"),
    path('battleUniverse/<int:pk>', BattleUniverseDetailView.as_view(), name="battle_universe_detail"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
