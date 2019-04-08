
from django.conf.urls import url
from . import views  
app_name = 'course'      
urlpatterns = [
    url(r'^courses$', views.index, name='index'),
    url(r'^courses/createcourse$', views.add),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/delete/$', views.delete, name='delete')
]
