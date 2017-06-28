
from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^$', views.user_new, name='user_new'),
	url(r'^(?P<pk>\d+)/$',views.get_user, name='get_user'),
	url(r'^instructions/$',views.instruction,name='instruction'),
	url(r'^home/$',views.home, name='home'),
]
