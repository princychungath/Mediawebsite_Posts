from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('addpost/',views.add_post,name='add_post'),
    path('viewpost',views.view_posts,name="view_posts"),
    path('detail_view/<int:post_id>/', views.detail_view, name='detail_view'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('update/<int:post_id>/', views.update, name='update'),
    
]