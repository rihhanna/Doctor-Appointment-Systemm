
from django.urls import path
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     # Default page is the login page
    path('login/', views.user_login, name='login'),
    
    path('book/', views.book_appointment, name='book_appointment'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('logout/', views.user_logout, name='logout'),
    path('doctor/', views.doctorsinfo , name='doctor_register'),
    path('doctor_list/', views.info, name='ushow'),
    path('update/<int:pk>', views.update, name='yupdate'),
    path('delete/<int:pk>', views.delete, name='udelete'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image_list/', views.image_list, name='image_list'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('appointments_update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('appointments_delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('contact/', views.contact, name='contact'),
    path('<int:pk>/', views.contact_detail_view, name='contact_detail'),
    path('contactlist/', views.contact_list_view, name='contact_list'),
    path('show/', views.show),
]