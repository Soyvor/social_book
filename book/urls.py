from django.conf.urls import handler400, handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.login, name='dashboard'),
    
]

# Custom error handlers
handler400 = 'book.views.error_400'
handler404 = 'book.views.error_404'
handler500 = 'book.views.error_500'
handler503 = 'book.views.error_503'
