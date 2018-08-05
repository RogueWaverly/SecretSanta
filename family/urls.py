from django.conf.urls import url
from family import views

urlpatterns = [
    url(r'^$', views.EditPoolsView.as_view()),
]
