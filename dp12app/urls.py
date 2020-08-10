from django.urls import path
from dp12app import views

app_name="dp12app"


urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
]