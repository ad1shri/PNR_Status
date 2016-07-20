from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    
    url(r'^your_pnrno$', views.your_pnrno),
	url(r'^post_list$', views.post_list),

)


