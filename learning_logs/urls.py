from django.urls import path
from . import views
# dot . is use to refer the same folder

app_name = 'learning_logs'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #topics page
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    

]