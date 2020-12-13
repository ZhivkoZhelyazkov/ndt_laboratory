from django.urls import path
from ndt_laboratory.common.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
]
