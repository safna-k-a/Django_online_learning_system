from django .urls import path
from superuser import views
urlpatterns = [
    path('course',views.course,name="course"),
    path('offer',views.offer,name="offer"),
    path('',views.admin,name="admin"),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('viewoffer',views.viewoffer,name='viewoffer'),
    path('deletefrom/<int:id>',views.deletecourse,name='deletecourse'),
    path('updatefrom/<int:id>',views.updatecourse,name='updatecourse'),
    path('deleteoffer/<int:id>',views.deleteoffer,name='deleteoffer'),
    path('updateoffer/<int:id>',views.updateoffer,name='updateoffer'),
]