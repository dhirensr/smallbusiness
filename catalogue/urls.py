from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r"^$", views.page_list, name="page_list"),
    url(
        r"^(?P<category_slug>[-\w]+)/$", views.page_list, name="pages_list_by_category"
    ),
    path("listing/new/", views.list_new, name="list_new"),
    url(r"thanks/", views.thank_you, name="thank_you"),
]
