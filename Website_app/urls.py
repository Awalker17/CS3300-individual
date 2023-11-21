from django.urls import path, include
from . import views
urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('show/<int:pk>', views.ShowDetailView.as_view(), name = 'show-detail'),
path('show', views.ShowListView.as_view(), name= "show-list"),
path('show/create_show', views.createShow, name='create_show'),
path('show/<int:show_id>/update_show', views.updateShow, name='update_show'),
path('show/<int:show_id>/delete_show', views.deleteShow, name='delete_show'),

path('user/<int:user_id>', views.UserDetailView, name = 'user_detail'),
path('user', views.UserListView.as_view(), name = 'user-list'),
path('user/create_user', views.createUser, name='create_user'),
path('user/<int:user_id>/delete_user', views.deleteUser, name='delete_user'),

path('', include('django.contrib.auth.urls')),
path('sign-up', views.sign_up, name="sign-up"),
]
