
from django.conf.urls import url
from apps import views

urlpatterns = [
    url(r'blogs/$',views.get_blogs, name='blogs'),
    url(r'detail/(\d+)/$',views.get_details, name='blog_get_detail'),
    url("",views.index,),
]
