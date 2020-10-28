from django.urls import path
from django.conf.urls import url
from . import views
from mytutor import views as user_views
from django.conf import settings

urlpatterns = [
    path('api/peris', views.TutorialList.as_view()),
     url(r'api/tutorial/tutorial-id/(?P<pk>[0-9]+)/$',views.TutoriaDescription.as_view())
    # path('api/tutorial/tutorial-id/',views.TutoriaDescription.as_view())
]