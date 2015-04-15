from django.conf.urls import url

urlpatterns = [
	url(r'^$',  'accounts.views.example', name='example'),
]