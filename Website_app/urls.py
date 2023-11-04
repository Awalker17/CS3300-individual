from django.urls import path
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
path('unfinished_shows', views.unfinishedShowList, name= "show_list_unfinished"),
path('show/create_show', views.createShow, name='create_show'),
path('show/<int:show_id>/update_show', views.updateShow, name='update_show'),
path('show/<int:show_id>/delete_show', views.deleteShow, name='delete_show'),
]
