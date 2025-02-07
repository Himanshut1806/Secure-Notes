from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='Signup'),    #name is same as ajax url in every urlpatterns
    path('login/',views.userlogin, name='Login'),
    path('logout/',views.userlogout, name='Logout'),
    path('edit_note',views.edit_note, name='EditNote'),
    path('delete_note',views.delete_note, name='DeleteNote'), 
]





















