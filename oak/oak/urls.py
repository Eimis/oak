from django.conf.urls import url
from django.contrib import admin

from oak import views as api_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^actions/set-action$', api_views.SetActionView.as_view(), name='set_action'),

]
