from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.index, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
