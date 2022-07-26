from django.urls import path
from.import views

urlpatterns=[
    path('',views.allprojects,name='all'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
    path('search/Edit/<str:pk>',views.Edit,name='Edit'),
    path('search/Assignment/<str:pk>',views.Assignment,name='Assignment'),
    path('assignment/',views.assignment,name='assignment'),
    path('search/',views.search,name='search'),
    path('view/',views.viewstudent,name='view'),
    path('search/Edit/delete/<str:pk>',views.delete,name='delete'),
    path('search/Edit/updaterecord/<str:pk>', views.updaterecord, name='updaterecord'),
    path('search/Assignment/assigndepart/<str:pk>', views.assigndepart, name='assigndepart'),
    path('view/active/<str:pk>', views.active, name='active'),

]