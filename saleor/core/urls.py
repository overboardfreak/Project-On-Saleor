from django.conf.urls import url
from impersonate.views import stop_impersonate

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stores/', views.stores, name='stores'),
    url(r'^belly/', views.belly, name='belly'),
    url(r'^brownie/', views.brownie, name='brownie'),
    url(r'^spoonful/', views.spoonful, name='spoonful'),
    url(r'^glen/', views.glen, name='glen'),
    url(r'^style-guide/', views.styleguide, name='styleguide'),
    url(r'^impersonate/(?P<uid>\d+)/', views.impersonate,
        name='impersonate-start'),
    url(r'^impersonate/stop/$', stop_impersonate,
        name='impersonate-stop'),
    url(r'^404', views.handle_404, name='handle-404'),
    url(r'^manifest\.json$', views.manifest, name='manifest'),
]
