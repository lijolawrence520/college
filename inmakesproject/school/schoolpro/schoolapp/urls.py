from django.urls import path
from. import views

urlpatterns=[
    path('',views.hom,name='hom'),
    path('login/',views.log,name='log'),
    path('register/',views.reg,name='reg'),
    path('form/',views.form,name='form'),
    path('logout/',views.logout,name='logout'),
    path('ajax/load_courses/',views.load_courses,name='ajax_load_courses'),
    path('cs/<int:id>/',views.cs,name="cs"),


    ]