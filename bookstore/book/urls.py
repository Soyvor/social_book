from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import fetch_data_view


urlpatterns = [
    path('index/', views.index , name='index'),  
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('fetch-data/', fetch_data_view, name='fetch_data'),
    path('advanced-components/', views.advanced_components_view, name='advanced_components'),
    path('apexcharts/', views.apexcharts_view, name='apexcharts'),
    path('basic-table/', views.basic_table_view, name='basic_table'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)