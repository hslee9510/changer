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
]
