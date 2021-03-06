"""projectmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from companyinfo.views import *

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^show_write_form', show_write_form, name = "show_write_form"),
    url(r'^DoWriteBoard', DoWriteBoard, name = "DoWriteBoard"),
    url(r'^viewWork', viewWork),
    url(r'^listSpecificPageWork', listSpecificPageWork),
    url(r'^updatePage', updatePage),
    url(r'^updateBoard', updateBoard),
    url(r'^DeleteSpecificRow', DeleteSpecificRow),
    url(r'^searchWithSubject/', searchWithSubject),
    url(r'^listSearchedSpecificPageWork', listSearchedSpecificPageWork),
    url(r'^companylist', CompanyList),
    url(r'^', home),
    ]
