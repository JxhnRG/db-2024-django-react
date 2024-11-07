
from rest_framework.urlpatterns import format_suffix_patterns # type: ignore
from django.urls import re_path # type: ignore

from .views import *

urlpatterns = [
  re_path(r'$', ListCreateClients.as_view(), name='create-list-clients')
]

urlpatterns = format_suffix_patterns(urlpatterns)
