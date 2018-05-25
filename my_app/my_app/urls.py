"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from names_api.views import (
    CreateNamesInDatabase,
    NamesListAPIView,
    PersonDetailAPIView,
    NamesEditView
)

urlpatterns = [
    url(r'^$', NamesEditView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^names_list/$', NamesListAPIView.as_view(), name='names-list'),
    url(r'^names_list/(?P<pk>\d+)/$', PersonDetailAPIView.as_view(), name='detail-view'),
    url(r'^create_names/$', CreateNamesInDatabase.as_view(), name='create-names'),
]
