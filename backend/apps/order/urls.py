
from rest_framework.urlpatterns import format_suffix_patterns # type: ignore
from django.urls import re_path # type: ignore

from .views import *

urlpatterns = [
  re_path(r'$', ListCreateOrder.as_view(), name='create-list-order')
]

urlpatterns = format_suffix_patterns(urlpatterns)
