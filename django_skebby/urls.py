from django.conf.urls import url

from .views import credit_left

urlpatterns = [
    url(r'credit_left/$', credit_left, {}, 'skebby-credit-left'),
]
