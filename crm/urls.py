from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('add_record', views.add_record, name='add_record'),
    path('record/<int:pk>', views.record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete')
]
