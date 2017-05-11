from django.conf.urls import url
from .views import homepage, post_list

urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/list$', post_list),
    url(r'^post/$', produit),
]
