from django.contrib import admin
from django.urls import path
from . import views 



app_nme = 'KMA_Clinic'
urlpatterns = [
	path('', views.patients, name='home'),
	path('save/', views.save_form,name='insert'),
	path('<int:age>/', views.patient_age,name='pass_age'),
	path('<int:id>/', views.detail,name='detail_id'),
	path('<int:id>/edit/', views.update_form,name='edit'),
	path('details/<int:id>/', views.detail,name='details'),
    #path('/', admin.site.urls),
 	path('visits/', views.save_visits,name='visits'),
 	path('visits/<int:id>/', views.detail_visits,name='visits_id'),
 	path('visits/edit/<int:id>/', views.update_visits,name='visits_edit'),
]