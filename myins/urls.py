from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^daily/$',views.daily,name='daily'),
    url(r'^todo/$',views.todo,name='todo'),
    url(r'^wish/$',views.wish,name='wish'),
    url(r'^inspiration/$',views.inspiration,name='inspiration'),
    url(r'^reference/$',views.reference,name='reference'),
    url(r'^trophy/$',views.trophy,name='trophy'),
    url(r'^daily/(?P<pk>\d+)/$',views.daily_detail,name='daily_detail'),
    url(r'^todo/(?P<pk>\d+)/$',views.todo_detail,name='todo_detail'),
    url(r'^wish/(?P<pk>\d+)/$',views.wish_detail,name='wish_detail'),
    url(r'^inspiration/(?P<pk>\d+)/$',views.inspiration_detail,name='inspiration_detail'),
    url(r'^reference/(?P<pk>\d+)/$',views.reference_detail,name='reference_detail'),
    url(r'^trophy/(?P<pk>\d+)/$',views.trophy_detail,name='trophy_detail'),
    url(r'^daily/new/$',views.daily_new,name='daily_new'),
    url(r'^daily/(?P<pk>\d+)/edit/$', views.daily_edit, name='daily_edit'),
    url(r'^todo/new/$',views.todo_new,name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^wish/new/$',views.wish_new,name='wish_new'),
    url(r'^wish/(?P<pk>\d+)/edit/$', views.wish_edit, name='wish_edit'),
    url(r'^inspiration/new/$',views.inspiration_new,name='inspiration_new'),
    url(r'^inspiration/(?P<pk>\d+)/edit/$', views.inspiration_edit, name='inspiration_edit'),
    url(r'^reference/new/$',views.reference_new,name='reference_new'),
    url(r'^reference/(?P<pk>\d+)/edit/$', views.reference_edit, name='reference_edit'),
    url(r'^trophy/new/$',views.trophy_new,name='trophy_new'),
    url(r'^trophy/(?P<pk>\d+)/edit/$', views.trophy_edit, name='trophy_edit'),
    url(r'^daily/(?P<pk>\d+)/remove/$', views.daily_remove, name='daily_remove'),
    
]
