from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('dashboard1/',dash1),
    path('dashboard2/',dash2),
    path('dashboard3/',dash3),
    path('dashboard4/',dash4),
    path('vis1/',vis1),
    path('vis2/',vis2),
    path('vis3/',vis3),
    path('vis4/',vis4),
    path('story1/',story1),
    path('story2/',story2),
    path('report1/',report1),
    path('report2/',report2),
    path('checkbmi/',checkbmi)
    
]
