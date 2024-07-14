from django.urls import path
from shaura import views
from shaura import views_api

app_name = 'shaura'
urlpatterns = [
   #punya readStudent
   path('', views.readStudent, name='read-data-student'),
   path('create/', views.createStudent, name='create-data-student'),
   path('update/<str:id>', views.updateStudent, name='update-data-student'),
   path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

   #Punya readCourse
   path('', views.readCourse, name='read-data-course'),
   path('create/', views.createCourse, name='create-data-course'),
   path('update/', views.updateCourse, name='update-data-course'),
   path('delete/', views.deleteCourse, name='delete-data-course'),

   #path API
   path('api/course',views_api.apiCourse, name='api-view-data-course'),

   #urls untuk consume API
   path('api/consume/course', views_api.consumeApiGet, name='api-consume-data-course'),
]