from django.urls import path
from . import views
from hrm.api import UserList, UserDetail
from django.conf.urls import url


urlpatterns = [
    path('', views.homeView.as_view(), name='home'),
    url(r'^api/user_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/user_list/(?P<id>\d+)/$', UserDetail.as_view(), name='user_list')

]


