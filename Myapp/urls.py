from django.urls import path
from Myapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.Index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginpage,name="login"),
    path('adminurl',views.admin_dash),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout1,name="logout"),
    path('buy/<int:id>',views.buy,name="buy"),
    path('buy1/<int:id>',views.buy1,name="buy1"),
    path('app/<int:id>/<int:pk>',views.app,name="app"),
    path('app1/<int:id>',views.app1,name="app1"),
    path('log/<int:id>',views.log,name="log"),
    path('log1/<int:id>',views.log1,name="log1"),
    path('search',views.search,name="search"),
    path('search_course',views.search_course,name='search_course'),
    path('loginsearch',views.loginsearch,name='loginsearch'),
    path('my_course/<int:id>',views.my_course,name="my_course"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart1/<int:id>/', views.add_to_cart1, name='add-to-cart1'),
    path('delete-cart/<int:id>/', views.delete_cart, name='delete-cart'),
    path('cartitem',views.cartitem,name="cartitem"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='index.html'),name='password_reset_complete'),]
