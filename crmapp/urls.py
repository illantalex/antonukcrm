from django.urls import path
from . import views

# from django.conf.urls import url

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company_list'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('messages/', views.MessageListView.as_view(), name='message_list'),
]

urlpatterns += [
    path('company_detail/<int:pk>', views.CompanyDetailView.as_view(), name='company_detail'),
    path('project_detail/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('message_detail/<int:pk>', views.MessageDetailView.as_view(), name='message_detail'),
]

urlpatterns += [
    path('manager_page/<int:pk>', views.ManagerCabinet.as_view(), name='manager_page'),
    path('manager/update/<int:pk>', views.UserUpdate.as_view(), name='user_update')
]

urlpatterns += [
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/update/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company_delete'),
]

urlpatterns += [
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
]

urlpatterns += [
    path('message/create/', views.MessageCreate.as_view(), name='message_create'),
    path('message/<int:pk>/update/', views.MessageUpdate.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', views.MessageDelete.as_view(), name='message_delete'),
]
