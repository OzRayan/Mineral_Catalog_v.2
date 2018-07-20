from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.mineral_list,
        name='mineral_list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail,
        name='mineral_detail'),
    url(r'random/', views.random_mineral,
        name='random_mineral'),
    url(r'starts_with/(?P<alpha>[a-zA-Z])/$', views.mineral_by_alphabet,
        name='mineral_alpha'),
    url(r'by_group/(?P<group>[\w ]+)/$', views.mineral_by_group,
        name='mineral_by_group'),
    url(r'by_color/(?P<color>\w+)/$', views.mineral_by_color,
        name='mineral_by_color'),
    url(r'by_crystal/(?P<crystal>\w+)/$', views.mineral_by_crystal_system,
        name='mineral_by_crystal'),
    url(r'search/$', views.mineral_search,
        name='mineral_search'),
]
