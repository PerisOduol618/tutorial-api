from django.urls import path
from . import views
from mytutor import views as user_views
from django.conf import settings

urlpatterns = [
    path('api/peris', views.TutorialList.as_view())
]