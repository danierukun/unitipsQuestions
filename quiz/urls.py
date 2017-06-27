from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^question/$', views.general_question_view),
    url(r'^question/(?P<question_id>[0-9])/$', views.single_question_view),
]
