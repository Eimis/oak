from django.conf.urls import url
from django.contrib import admin

from oak import views as api_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^game/init$',
        api_views.GameInitializationView.as_view(),
        name='init_game'
    ),
    url(
        r'^game/set-action$',
        api_views.GameActionView.as_view(),
        name='set_game_acion'
    ),
]
